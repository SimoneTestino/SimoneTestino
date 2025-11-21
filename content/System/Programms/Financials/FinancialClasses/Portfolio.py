#!/usr/bin/env python3
"""
Portfolio.py
The complete portfolio class with all calculation methods.
"""

import sys
import os
from datetime import date
from typing import List, Any, Optional, Dict
from decimal import Decimal
from moneyed import Money, get_currency

# --- Path Setup ---
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit
from FinancialClasses.LiquidAssets import LiquidAssets
from FinancialClasses.IlliquidAsset import IlliquidAsset
from FinancialClasses.Salary import Salary
from Helper.CurrencyConverter import CurrencyConverter

class Portfolio:
    """
    A portfolio of assets that computes aggregate statistics including Net Worth,
    AUM (Exposure), and performance metrics like Profit and Return.
    """
    def __init__(self, valuation_date: date, assets: Optional[List] = None):
        self.valuation_date = valuation_date
        self.assets = assets or []
        self._converter = CurrencyConverter()

    def add_asset(self, asset: Any) -> None:
        self.assets.append(asset)

    def remove_asset(self, asset: Any) -> None:
        self.assets.remove(asset)

    def _value_in_currency(self, money: Money, target: str) -> Decimal:
        if money.currency.code == target:
            return money.amount
        return self._converter.convert(money, target).amount

    # --- Value (Net Worth) Methods ---
    def total_value(self, currency: str = 'EUR') -> Money:
        """Calculates Net Worth (unleveraged, risk-adjusted, debits subtracted)."""
        return Money(sum(self.get_value_by_asset_class(currency).values()), get_currency(currency))

    def get_value_by_asset_class(self, currency: str = 'EUR') -> Dict[str, Decimal]:
        """Calculates the Net Worth contribution for each asset class."""
        class_values = { 'market': Decimal('0'), 'liquidity': Decimal('0'), 'illiquid': Decimal('0'), 'credit': Decimal('0'), 'debit': Decimal('0')}
        for a in self.assets:
            asset_class = getattr(a, 'asset_class', None)
            val = None
            if asset_class == 'market': val = getattr(a, 'actual_current_value', None)
            elif asset_class in ['liquidity', 'illiquid']: val = a.get_current_value(on_date=self.valuation_date)
            elif asset_class == 'credit': val = a.expected_value(on_date=self.valuation_date)
            elif asset_class == 'debit': val = a.total_outstanding(on_date=self.valuation_date)
            
            if val is not None and asset_class in class_values:
                class_values[asset_class] += self._value_in_currency(val, currency)
        return class_values

    # --- Exposure (AUM) Methods ---
    def total_aum(self, currency: str = 'EUR') -> Money:
        """Calculates Assets Under Management (AUM) as the sum of all positive exposures."""
        exposure_values = self.get_exposure_by_asset_class(currency)
        total = sum(v for k, v in exposure_values.items() if k != 'debit')
        return Money(total, get_currency(currency))

    def get_exposure_by_asset_class(self, currency: str = 'EUR') -> Dict[str, Decimal]:
        """Calculates the AUM / Exposure contribution for each asset class."""
        class_exposures = { 'market': Decimal('0'), 'liquidity': Decimal('0'), 'illiquid': Decimal('0'), 'credit': Decimal('0'), 'debit': Decimal('0')}
        for a in self.assets:
            asset_class = getattr(a, 'asset_class', None)
            val = None
            if asset_class == 'market': val = getattr(a, 'current_value', None) # Leveraged
            elif asset_class in ['liquidity', 'illiquid']: val = a.get_current_value(on_date=self.valuation_date)
            elif asset_class == 'credit': val = a.total_outstanding(on_date=self.valuation_date) # Unadjusted
            elif asset_class == 'debit': val = a.total_outstanding(on_date=self.valuation_date)
            
            if val is not None and asset_class in class_exposures:
                class_exposures[asset_class] += self._value_in_currency(val, currency)
        return class_exposures

    # --- Performance Methods ---
    def total_invested(self, currency: str = 'EUR') -> Money:
        """Calculates the total capital invested in the portfolio."""
        total = Decimal('0')
        for a in self.assets:
            asset_class = getattr(a, 'asset_class', '')
            if asset_class in ['liquidity', 'illiquid']:
                init = getattr(a, 'purchase_price', getattr(a, 'amount', None))
                if init: total += self._value_in_currency(init, currency)
            elif asset_class == 'market':
                init = getattr(a, 'actual_invested', None)
                if init: total += self._value_in_currency(init, currency)
            elif asset_class == 'debit':
                debt = getattr(a, 'principal', None)
                if debt: total -= abs(self._value_in_currency(debt, currency))
        return Money(total, get_currency(currency))

    def total_profit(self, currency: str = 'EUR') -> Money:
        """Calculates total profit or loss based on invested capital vs. net worth."""
        return Money(self.total_value(currency).amount - self.total_invested(currency).amount, get_currency(currency))

    def total_return(self) -> float:
        """Calculates the overall return on invested capital as a percentage."""
        invested = self.total_invested().amount
        if invested <= 0: return 0.0
        return float(self.total_profit().amount / invested)

    # --- Utility Methods ---
    def update_all_market_values(self) -> None:
        for asset in self.assets:
            if hasattr(asset, 'update_market_value'):
                asset.update_market_value()

    def summary(self, currency: str = 'EUR') -> str:
        """Provides a brief summary including both AUM and Net Worth."""
        aum = self.total_aum(currency)
        net_worth = self.total_value(currency)
        return (
            f"Portfolio Summary as of {self.valuation_date}:\n"
            f"  Assets Under Management (AUM): {aum}\n"
            f"  Net Worth: {net_worth}"
        )

# --- Example Usage ---
if __name__ == '__main__':
    today = date.today()
    
    # Create assets for a comprehensive test
    cash_eur = Liquidity(name='Cash EUR', amount=Money(10000, 'EUR'), purchase_price=Money(10000, 'EUR'), storage='Wallet')
    leveraged_etf = LiquidAssets(name='2x ETF', ticker='TQQQ', quantity=100, purchase_price=Money(50, 'USD'), leverage=2.0)
    leveraged_etf.actual_invested = Money(5000, 'USD')
    leveraged_etf.actual_current_value = Money(6000, 'USD')
    leveraged_etf.current_value = Money(12000, 'USD')
    my_debit = Debit(creditor='Bank', principal=Money(5000, 'EUR'))
    
    portfolio = Portfolio(valuation_date=today)
    portfolio.add_asset(cash_eur)
    portfolio.add_asset(leveraged_etf)
    portfolio.add_asset(my_debit)
    
    print("--- Brief Summary ---")
    print(portfolio.summary())

    print("\n--- Detailed Performance Metrics ---")
    print(f"  Total Invested: {portfolio.total_invested()}")
    print(f"  Total Profit/Loss: {portfolio.total_profit()}")
    print(f"  Overall Return: {portfolio.total_return():.2%}")