#!/usr/bin/env python3
"""
IlliquidAsset.py

Represents an illiquid asset with a valuation history, optional growth/depreciation,
and an end-of-life date.
"""

from datetime import date, timedelta
from typing import List, Tuple, Optional
from moneyed import Money
from decimal import Decimal
import warnings

class IlliquidAsset:
    """
    Represents a physical or illiquid asset with a history of valuations.

    The value can be projected forward from the last manual valuation using a
    long-term growth rate. The value becomes zero after the end-of-life date.
    """
    def __init__(
        self,
        name: str,
        valuations: List[Tuple[date, Money]],
        purchase_price: Optional[Money] = None,
        purchase_date: Optional[date] = None,
        description: Optional[str] = None,
        long_term_growth_rate: Optional[float] = None,
        end_of_life_date: Optional[date] = None
    ):
        if not valuations:
            raise ValueError("The 'valuations' list cannot be empty.")

        self.name = name
        self.asset_class = 'illiquid'
        self.valuations = sorted(valuations, key=lambda v: v[0])
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.description = description
        self.long_term_growth_rate = long_term_growth_rate
        self.end_of_life_date = end_of_life_date

    @property
    def last_manual_valuation(self) -> Tuple[date, Money]:
        """Returns the most recent manually-set valuation tuple."""
        return self.valuations[-1]

    def get_current_value(self, on_date: Optional[date] = None) -> Money:
        """
        Calculates the asset's value on a specific date.
        """
        valuation_date = on_date or date.today()
        base_date, base_value = self.last_manual_valuation

        if self.end_of_life_date and valuation_date >= self.end_of_life_date:
            return Money(0, base_value.currency)

        if self.long_term_growth_rate is not None and valuation_date > base_date:
            years_passed = Decimal(str((valuation_date - base_date).days / 365.25))
            growth_rate = Decimal(str(self.long_term_growth_rate))
            growth_factor = (Decimal('1') + growth_rate) ** years_passed
            return base_value * growth_factor

        return base_value

    @property
    def current_value(self) -> Money:
        """
        Returns the value as of today for backward compatibility.
        """
        return self.get_current_value()

    def add_valuation(self, valuation_date: date, value: Money, verbose: bool = True) -> None:
        """
        Adds a new valuation to the asset's history.
        Set verbose=False to suppress the print message during forecasts.
        """
        self.valuations.append((valuation_date, value))
        self.valuations.sort(key=lambda v: v[0])
        # --- EDIT: Printing is now optional ---
        if verbose:
            print(f"Updated valuation for '{self.name}' to {value} on {valuation_date}.")

    def summary(self) -> str:
        """Returns a formatted summary of the asset."""
        today = date.today()
        current_val = self.get_current_value(on_date=today)
        base_date, base_value = self.last_manual_valuation

        value_method = "Manually Set"
        if self.long_term_growth_rate is not None and today > base_date:
            value_method = f"Projected with {self.long_term_growth_rate:+.1%} annual growth"
        if self.end_of_life_date and today >= self.end_of_life_date:
            value_method = "End of Life Reached"

        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Current Value: {current_val} ({value_method})",
            f"- Last Manual Valuation: {base_value} on {base_date}",
        ]
        if self.purchase_price:
            profit = current_val.amount - self.purchase_price.amount
            lines.append(f"- Unrealized Gain/Loss: {Money(profit, current_val.currency)}")
        
        if self.end_of_life_date:
            lines.append(f"- End of Life Date: {self.end_of_life_date}")
            
        return "\n".join(lines)

# --- Example Usage ---
if __name__ == "__main__":
    today = date(2025, 7, 26)

    # ... (example usage remains the same)
    print("--- 1. Depreciating Asset: Car ---")
    car = IlliquidAsset(
        name="Honda Civic",
        purchase_price=Money(20000, "EUR"),
        valuations=[(date(2024, 1, 1), Money(12000, "EUR"))],
        long_term_growth_rate=-0.15,
        end_of_life_date=date(2032, 1, 1)
    )
    print(car.summary())

    print("\n" + "="*50 + "\n")

    print("--- 3. Updating an asset ---")
    print(f"The car's current value is {car.current_value}.")
    # The print statement in add_valuation will appear here by default
    car.add_valuation(today, Money(11500, "EUR")) 
    print(f"The car's new value is {car.current_value}.")