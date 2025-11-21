#!/usr/bin/env python3
"""
Liquidity.py
Represents pure cash holdings.
"""

from datetime import date
from typing import Optional, Literal
from moneyed import Money
from decimal import Decimal

# Note: This class no longer needs forex-python, as all currency conversion
# is now handled centrally by the Portfolio's CurrencyConverter.

StorageOption = Literal['ISP', 'IBKR', 'Degiro', 'Physical Cash', 'Deposit', 'Bank Account', 'Wallet']

class Liquidity:
    """
    Represents pure cash holdings in various storage locations. This class
    does not perform currency conversions; that is handled by the Portfolio.
    """
    def __init__(
        self,
        name: str,
        amount: Money,
        storage: StorageOption,
        description: Optional[str] = None,
        acquisition_date: Optional[date] = None,
        acquisition_origin: Optional[str] = None,
        purchase_price: Optional[Money] = None # For consistency in Portfolio's total_invested
    ):
        self.name = name
        self.asset_class = 'liquidity'
        self.amount = amount
        self.storage = storage
        self.description = description or ''
        self.acquisition_date = acquisition_date
        self.acquisition_origin = acquisition_origin
        
        # If no specific purchase price is given, the purchase price is its face value.
        self.purchase_price = purchase_price or amount
        
        # For a cash object, its current_value is always its face value.
        self.current_value = amount

    def get_current_value(self, on_date: Optional[date] = None) -> Money:
        """
        Returns the current value of the cash.

        For liquidity, this is always its face value. The 'on_date' parameter
        is ignored but included for interface consistency with other asset classes.
        """
        return self.current_value

    def summary(self) -> str:
        """
        Return a formatted summary of the liquidity asset.
        """
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Amount: {self.amount}",
            f"- Storage: {self.storage}",
        ]
        if self.description:
            lines.append(f"- Notes: {self.description}")
        return "\n".join(lines)

# --- Example Usage ---
if __name__ == "__main__":
    cash_in_wallet = Liquidity(
        name="Cash in Wallet",
        amount=Money(150, "EUR"),
        storage="Wallet"
    )

    print(cash_in_wallet.summary())
    
    # Demonstrate the get_current_value method
    print(f"Value from get_current_value(): {cash_in_wallet.get_current_value()}")