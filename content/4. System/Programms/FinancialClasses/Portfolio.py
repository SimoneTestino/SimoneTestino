import sys
import os
# Ensure parent directory (main project) is on sys.path to import Helper/
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from datetime import date
from typing import List, Dict, Union
from decimal import Decimal
from moneyed import Money, get_currency

from Helper.CurrencyConverter import CurrencyConverter

from FinancialClasses.Liquidity import Liquidity
from FinancialClasses.Credit import Credit
from FinancialClasses.Debit import Debit
from FinancialClasses.LiquidAssets import LiquidAssets

class Portfolio:
    """
    A portfolio consisting of various assets: Liquidity, Credit, Debit, LiquidAssets.

    Methods compute aggregate statistics (current total value, profit, returns),
    and breakdowns by geography, asset class, instrument type, and currency.
    Uses CurrencyConverter for FX conversions.
    """
    def __init__(self, valuation_date: date, assets: List[Union[Liquidity, Credit, Debit, LiquidAssets]] = None):
        self.valuation_date = valuation_date
        self.assets = assets or []
        # Initialize converter
        self._converter = CurrencyConverter()

    def add_asset(self, asset: Union[Liquidity, Credit, Debit, LiquidAssets]) -> None:
        self.assets.append(asset)

    def remove_asset(self, asset) -> None:
        self.assets.remove(asset)

    def _value_in_currency(self, money: Money, target: str) -> Decimal:
        """
        Convert a Money instance to target currency amount as Decimal.
        """
        if money.currency.code == target:
            return Decimal(str(money.amount))
        converted = self._converter.convert(money, target)
        return Decimal(str(converted.amount))

    def total_value(self, currency: str = 'EUR') -> Money:
        """Sum current values across all assets in given currency."""
        total = Decimal('0')
        for a in self.assets:
            val = getattr(a, 'current_value', None)
            if val is None and hasattr(a, 'total_outstanding'):
                val = a.total_outstanding()
            if val is None and hasattr(a, 'amount'):
                val = a.amount
            if val is None:
                continue
            total += self._value_in_currency(val, currency)
        return Money(total, get_currency(currency))

    def total_invested(self, currency: str = 'EUR') -> Money:
        """Sum initial or principal values for assets in currency."""
        total = Decimal('0')
        for a in self.assets:
            if hasattr(a, 'initial_value'):
                init = a.initial_value
            elif hasattr(a, 'principal'):
                init = a.principal
            elif hasattr(a, 'amount'):
                init = a.amount
            else:
                continue
            total += self._value_in_currency(init, currency)
        return Money(total, get_currency(currency))

    def total_profit(self, currency: str = 'EUR') -> Money:
        """Compute total profit = total_value - total_invested."""
        invested = self.total_invested(currency).amount
        value = self.total_value(currency).amount
        return Money(value - invested, get_currency(currency))

    def total_return(self) -> float:
        """Return ratio over portfolio."""
        invested = self.total_invested().amount
        if invested == 0:
            return 0.0
        return float(self.total_profit().amount / invested)

    def breakdown_by_geography(self, currency: str = 'EUR') -> Dict[str, Decimal]:
        """Percentage of total value by geography (for LiquidAssets only)."""
        totals: Dict[str, Decimal] = {}
        overall = self.total_value(currency).amount
        if overall == 0:
            return {}
        for a in self.assets:
            geo = getattr(a, 'geography', 'N/A')
            if hasattr(a, 'current_value'):
                val = a.current_value
            elif hasattr(a, 'total_outstanding'):
                val = a.total_outstanding()
            else:
                continue
            amt = self._value_in_currency(val, currency)
            totals[geo] = totals.get(geo, Decimal('0')) + amt
        return {g: (amt / overall * 100) for g, amt in totals.items()}

    def breakdown_by_asset_class(self) -> Dict[str, int]:
        """Count of assets by asset_class."""
        counts: Dict[str, int] = {}
        for a in self.assets:
            cls = getattr(a, 'asset_class', type(a).__name__)
            counts[cls] = counts.get(cls, 0) + 1
        return counts

    def breakdown_by_instrument(self) -> Dict[str, int]:
        """Count by instrument_type where applicable."""
        counts: Dict[str, int] = {}
        for a in self.assets:
            it = getattr(a, 'instrument_type', None)
            if it:
                counts[it] = counts.get(it, 0) + 1
        return counts

    def breakdown_by_currency(self, target_currency: str = 'EUR') -> Dict[str, Dict[str, Union[Money, Decimal, int]]]:
        """
        Breakdown of assets by their original currency and converted values.
        Returns a dict: currency -> metrics.
        """
        breakdown: Dict[str, Dict[str, Union[Money, Decimal, int]]] = {}
        total_val = self.total_value(target_currency).amount
        for a in self.assets:
            if hasattr(a, 'current_value'):
                val = a.current_value
            elif hasattr(a, 'total_outstanding'):
                val = a.total_outstanding()
            elif hasattr(a, 'amount'):
                val = a.amount
            elif hasattr(a, 'principal'):
                val = a.principal
            else:
                continue
            code = val.currency.code
            entry = breakdown.setdefault(code, {
                'original_total': Money(0, get_currency(code)),
                'converted_total': Decimal('0'),
                'count': 0
            })
            entry['original_total'] += val
            conv = self._value_in_currency(val, target_currency)
            entry['converted_total'] += conv
            entry['count'] += 1
        for data in breakdown.values():
            data['percentage'] = (data['converted_total'] / total_val * 100) if total_val > 0 else Decimal('0')
        return breakdown

    def summary(self) -> str:
        """Text summary of key portfolio metrics."""
        lines: List[str] = []
        lines.append(f"Portfolio valuation at {self.valuation_date}")
        lines.append(f"- Total invested: {self.total_invested()}")
        lines.append(f"- Total current value: {self.total_value()}")
        lines.append(f"- Total profit: {self.total_profit()}")
        lines.append(f"- Total return: {self.total_return():.2%}")

        geo = self.breakdown_by_geography()
        if geo:
            lines.append("- By geography:")
            for g, pct in geo.items():
                lines.append(f"    * {g}: {pct:.2f}%")

        ac = self.breakdown_by_asset_class()
        if ac:
            lines.append("- By asset class:")
            for cls, cnt in ac.items():
                lines.append(f"    * {cls}: {cnt}")

        inst = self.breakdown_by_instrument()
        if inst:
            lines.append("- By instrument type:")
            for it, cnt in inst.items():
                lines.append(f"    * {it}: {cnt}")

        cb = self.breakdown_by_currency()
        if cb:
            lines.append("- By currency:")
            for code, data in cb.items():
                lines.append(f"    * {code}: {data['original_total']} ({data['percentage']:.2f}%, {data['count']} assets)")

        return "\n".join(lines)

    def detailed_currency_summary(self, target_currency: str = 'EUR') -> str:
        """
        Detailed currency breakdown summary.
        """
        lines: List[str] = []
        lines.append(f"Currency Breakdown (converted to {target_currency}):")
        lines.append("-"*50)
        breakdown = self.breakdown_by_currency(target_currency)
        for code, data in breakdown.items():
            lines.append(f"{code}:")
            lines.append(f"  Original Total: {data['original_total']}")
            lines.append(f"  Converted Total: {Money(data['converted_total'], get_currency(target_currency))}")
            lines.append(f"  Portfolio %: {data['percentage']:.2f}%")
            lines.append(f"  Number of Assets: {data['count']}")
            lines.append("")
        return "\n".join(lines)
    60
# Example usage
if __name__ == '__main__':
    # 1. Pure cash holding
    cash = Liquidity(
        name='Emergency Fund',
        amount=Money(5000, 'USD'),
        storage='Physical Cash',
        description='For unexpected expenses',
        acquisition_date=date(2025, 1, 15),
        acquisition_origin='Monthly savings'
    )

    # 2. Planned credit
    credit_schedule = [
        (date(2025, 3, 1), Money(500, 'USD')),
        (date(2025, 9, 1), Money(550, 'USD')),
    ]
    credit = Credit(
        debtor='Alice',
        principal=Money(1000, 'USD'),
        credit_type='planned',
        interest_rate=0.05,
        repayment_schedule=credit_schedule
    )

    # 3. Conditional debit
    debit = Debit(
        creditor='Bank',
        principal=Money(2000, 'EUR'),
        debit_type='conditional',
        interest_rate=0.03
    )

    # 4. Market asset (ETF)
    etf = LiquidAssets(
        name='iShares Core MSCI World UCITS ETF',
        ticker='EUNL.DE',
        quantity=50,
        purchase_price=Money(70, 'EUR'),
        purchase_date=date(2024, 6, 1),
        instrument_type='ETF',
        etf_subtype='stocks',
        leverage=1.0,
        geography='Global'
    )
    etf.update_market_value()

    # Build portfolio
    portfolio = Portfolio(valuation_date=date.today())
    portfolio.add_asset(cash)
    portfolio.add_asset(credit)
    portfolio.add_asset(debit)
    portfolio.add_asset(etf)

    # Print portfolio summary
    print(portfolio.summary())
    print("\n" + "="*60 + "\n")
    print(portfolio.detailed_currency_summary())
