from datetime import date
from typing import Optional, Literal, List, Tuple
from moneyed import Money, USD, EUR, get_currency
from forex_python.converter import CurrencyRates
import warnings

StorageOption = Literal['ISP', 'IBKR', 'Degiro', 'Physical Cash', 'Deposit']

class Liquidity:
    """
    Represents pure cash holdings in various storage locations, with optional acquisition metadata.
    """
    def __init__(
        self,
        name: str,
        amount: Money,
        storage: StorageOption,
        description: Optional[str] = None,
        acquisition_date: Optional[date] = None,
        acquisition_origin: Optional[str] = None
    ):
        self.name = name
        self.asset_class = 'liquidity'
        self.amount = amount
        self.storage = storage
        self.description = description or ''
        self.acquisition_date = acquisition_date
        self.acquisition_origin = acquisition_origin
        self.current_value = amount
        self._fx = CurrencyRates()

    def compute_return(self) -> float:
        """
        Simple return: (current - initial) / initial
        """
        init = self.amount.amount
        curr = self.current_value.amount
        if init == 0:
            return 0.0
        return (curr - init) / init

    def convert_to(self, target_currency: str) -> Money:
        """
        Convert current value to a different currency using live FX rates.
        """
        src = self.amount.currency.code
        tgt = target_currency.upper()
        rate = self._fx.get_rate(src, tgt)
        converted = self.current_value.amount * rate
        return Money(converted, get_currency(tgt))

    def to_eur(self) -> Money:
        """
        Convenience method to convert current value to EUR.
        """
        return self.convert_to('EUR')

    def to_usd(self) -> Money:
        """
        Convenience method to convert current value to USD.
        """
        return self.convert_to('USD')

    def summary(self) -> str:
        """
        Return a formatted summary of the liquidity asset.
        """
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Amount: {self.amount}",
            f"- Storage: {self.storage}",
        ]
        if self.acquisition_date or self.acquisition_origin:
            acq = []
            if self.acquisition_date:
                acq.append(f"on {self.acquisition_date}")
            if self.acquisition_origin:
                acq.append(f"from {self.acquisition_origin}")
            lines.append(f"- Acquired {' '.join(acq)}")
        if self.description:
            lines.append(f"- Notes: {self.description}")
        ret = self.compute_return()
        lines.append(f"- Return: {ret:.2%}")
        return "\n".join(lines)



