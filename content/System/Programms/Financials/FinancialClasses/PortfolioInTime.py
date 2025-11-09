#!/usr/bin/env python3
"""
PortfolioInTime.py

A class to model a portfolio's evolution over time, enabling historical
analysis and future scenario forecasting.
"""

import sys
import os
from datetime import date
from typing import List, Tuple, Dict, Any, Literal
from decimal import Decimal
from moneyed import Money
from dateutil.relativedelta import relativedelta
import copy

# --- Path Setup ---
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
from FinancialClasses.Portfolio import Portfolio
from FinancialClasses.LiquidAssets import LiquidAssets
from FinancialClasses.IlliquidAsset import IlliquidAsset
from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit

# Scenarios
SCENARIO_STATIC = {'stock': 0.0, 'bond': 0.0, 'real_estate': 0.0, 'other': 0.0}
SCENARIO_GROWTH = {'stock': 0.10, 'bond': 0.04, 'real_estate': 0.02, 'other': 0.0}


class PortfolioInTime:
    """
    Manages a portfolio's state across time through a series of modifications.
    """
    def __init__(self, initial_portfolio: Portfolio):
        self.initial_portfolio = initial_portfolio
        self.start_date = initial_portfolio.valuation_date
        self.modifications: List[Tuple[date, str, Any]] = []

    def add_modification(self, mod_date: date, action: Literal['add', 'remove'], asset: Any):
        """Adds a portfolio modification event to the timeline."""
        if action not in ['add', 'remove']:
            raise ValueError("Action must be 'add' or 'remove'.")
        self.modifications.append((mod_date, action, asset))
        self.modifications.sort(key=lambda x: x[0])

    def _clone_asset(self, asset: Any) -> Any:
        """
        Creates a safe copy of an asset to avoid modifying originals during forecasts.
        """
        asset_class = type(asset)

        if asset_class == LiquidAssets:
            clone = LiquidAssets(
                name=asset.name, ticker=asset.ticker, quantity=asset.quantity,
                purchase_price=asset.purchase_price, purchase_date=asset.purchase_date,
                isin=asset.isin, exchange=getattr(asset, 'exchange', None),
                instrument_type=asset.instrument_type, etf_subtype=asset.etf_subtype,
                leverage=asset.leverage, geography=asset.geography
            )
            clone.current_value = asset.current_value
            clone.actual_current_value = asset.actual_current_value
            return clone
        elif asset_class == Credit:
            return Credit(
                debtor=asset.debtor, principal=asset.principal, credit_type=asset.credit_type,
                interest_rate=asset.interest_rate, repayment_schedule=asset.schedule,
                origination_date=asset.origination_date, certainty=asset.certainty
            )
        elif asset_class == Debit:
             return Debit(
                creditor=asset.creditor, principal=asset.principal, debit_type=asset.debit_type,
                interest_rate=asset.interest_rate, repayment_schedule=asset.schedule,
                origination_date=asset.origination_date
            )
        else:
            return copy.deepcopy(asset)

    def get_portfolio_at_date(
        self,
        target_date: date,
        scenario_name: Literal['static', 'constant_growth'] = 'static'
    ) -> Portfolio:
        """
        Constructs and values the portfolio for a specific target date.
        """
        scenario = SCENARIO_GROWTH if scenario_name == 'constant_growth' else SCENARIO_STATIC
        
        assets_on_date = []
        for asset in self.initial_portfolio.assets:
            start_asset_date = getattr(asset, 'purchase_date', None) or \
                               getattr(asset, 'origination_date', None) or \
                               self.start_date
            
            if start_asset_date <= target_date:
                assets_on_date.append(self._clone_asset(asset))
        
        for mod_date, action, asset in self.modifications:
            if mod_date <= target_date:
                if action == 'add':
                    assets_on_date.append(self._clone_asset(asset))
                elif action == 'remove':
                    assets_on_date = [a for a in assets_on_date if getattr(a, 'name') != getattr(asset, 'name')]

        timed_portfolio = Portfolio(valuation_date=target_date)
        timed_portfolio.assets = assets_on_date

        for asset in timed_portfolio.assets:
            if isinstance(asset, (LiquidAssets, IlliquidAsset)):
                if target_date > self.start_date:
                    self._apply_growth_scenario(asset, target_date, scenario_name, scenario)
        
        return timed_portfolio

    def _get_asset_growth_category(self, asset: Any) -> str:
        if isinstance(asset, LiquidAssets):
            subtype = getattr(asset, 'etf_subtype', 'stocks')
            return 'bond' if 'bond' in subtype else 'stock'
        if isinstance(asset, IlliquidAsset):
            return 'real_estate'
        return 'other'

    def _apply_growth_scenario(self, asset: Any, target_date: date, scenario_name: str, scenario: Dict[str, float]):
        if isinstance(asset, IlliquidAsset):
            if asset.end_of_life_date and target_date >= asset.end_of_life_date:
                asset.add_valuation(target_date, Money(0, asset.current_value.currency), verbose=False)
                return

        category = self._get_asset_growth_category(asset)
        rate = scenario.get(category, 0.0)

        if scenario_name == 'constant_growth' and isinstance(asset, IlliquidAsset) and asset.long_term_growth_rate is not None:
            rate = asset.long_term_growth_rate
        
        if rate != 0:
            base_date = self.start_date
            base_value = None
            for initial_asset in self.initial_portfolio.assets:
                if getattr(initial_asset, 'name') == getattr(asset, 'name'):
                    if isinstance(initial_asset, LiquidAssets):
                        base_value = initial_asset.actual_current_value
                    elif isinstance(initial_asset, IlliquidAsset):
                        base_value = initial_asset.get_current_value(on_date=self.start_date)
                        base_date = initial_asset.last_manual_valuation[0]
                    break
            
            if not base_value:
                 return

            years = (target_date - base_date).days / 365.25
            growth_factor = (Decimal('1') + Decimal(str(rate))) ** Decimal(str(years))
            new_value = base_value * growth_factor
            
            if hasattr(asset, 'set_value') and isinstance(asset, LiquidAssets):
                asset.set_value(new_value)
            elif isinstance(asset, IlliquidAsset):
                # --- EDIT: Use verbose=False to keep the output clean ---
                asset.add_valuation(target_date, new_value, verbose=False)


# --- Example Usage ---
if __name__ == '__main__':
    def set_value(self, new_unleveraged_price: Money):
        self.actual_current_value = new_unleveraged_price
        self.current_value = new_unleveraged_price * Decimal(str(self.leverage))
    LiquidAssets.set_value = set_value

    start_date = date(2025, 7, 26)
    
    cash = Liquidity(name="Starting Cash", amount=Money(20000, "EUR"), storage="Bank")
    sp500_etf = LiquidAssets(name="S&P 500 ETF", ticker="VOO", quantity=50, instrument_type="ETF", etf_subtype="stocks")
    apartment = IlliquidAsset(
        name="My Apartment", purchase_price=Money(150000, "EUR"),
        valuations=[(start_date, Money(180000, "EUR"))],
        long_term_growth_rate=0.02
    )
    
    initial_portfolio = Portfolio(valuation_date=start_date, assets=[cash, sp500_etf, apartment])
    initial_portfolio.update_all_market_values()
    
    print("--- Initial Portfolio ---")
    print(initial_portfolio.summary())

    timeline = PortfolioInTime(initial_portfolio)
    
    sell_date = start_date + relativedelta(years=+2)
    timeline.add_modification(sell_date, 'remove', sp500_etf)

    future_date = start_date + relativedelta(years=+10)
    
    print(f"\n--- Forecasting for {future_date} ---")
    
    print("\n--- Scenario: Constant Growth ---")
    growth_forecast = timeline.get_portfolio_at_date(future_date, scenario_name='constant_growth')
    print(growth_forecast.summary())