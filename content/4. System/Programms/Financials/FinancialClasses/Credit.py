#!/usr/bin/env python3
"""
Credit.py
Represents a credit (loan) extended to a debtor, with an adjustable
certainty factor for risk management.
"""

from datetime import date, timedelta
from typing import List, Tuple, Optional, Literal
from decimal import Decimal
from moneyed import Money
from dateutil.relativedelta import relativedelta
import warnings

CreditType = Literal['planned', 'conditional']

class Credit:
    """
    Represents a credit, such as a loan, owed by a debtor.

    Separates the full outstanding balance from the risk-adjusted 'expected_value'
    which is used for net worth calculations.
    """
    def __init__(
        self,
        debtor: str,
        principal: Money,
        credit_type: CreditType = 'planned',
        interest_rate: float = 0.0,
        repayment_schedule: Optional[List[Tuple[date, Money]]] = None,
        origination_date: Optional[date] = None,
        certainty: float = 1.0
    ):
        if not (0.0 <= certainty <= 1.0):
            raise ValueError("Certainty must be between 0.0 and 1.0.")

        self.debtor = debtor
        self.name = f"Credit to {debtor}"
        self.asset_class = 'credit'
        self.principal = Money(abs(Decimal(principal.amount)), principal.currency)
        self.credit_type = credit_type
        self.interest_rate = interest_rate
        self.origination_date = origination_date or date.today()
        self.certainty = certainty
        
        self.schedule: List[Tuple[date, Money]] = []
        if self.credit_type == 'planned' and repayment_schedule:
            for dt, m in repayment_schedule:
                self.schedule.append((dt, Money(abs(m.amount), m.currency)))
            self.schedule.sort()

    def total_outstanding(self, on_date: Optional[date] = None) -> Money:
        """
        Calculates the full, unadjusted remaining loan balance (principal + interest - paid).
        """
        valuation_date = on_date or date.today()
        if valuation_date < self.origination_date:
            return self.principal

        rate = Decimal(str(self.interest_rate))
        base = self.principal.amount
        days = (valuation_date - self.origination_date).days
        interest_to_date = base * rate * Decimal(days) / Decimal('365')
        total_owed = base + interest_to_date

        if self.credit_type == 'planned' and self.schedule:
            paid_amount = sum(p.amount for d, p in self.schedule if d <= valuation_date)
            total_owed -= paid_amount
            
        return Money(total_owed, self.principal.currency)

    def expected_value(self, on_date: Optional[date] = None) -> Money:
        """
        Calculates the risk-adjusted value for net worth calculations.
        This is the total outstanding amount multiplied by the certainty factor.
        """
        outstanding = self.total_outstanding(on_date)
        return outstanding * Decimal(str(self.certainty))

    def generate_schedule(self, start_date: date, end_date: date) -> List[Tuple[date, Money]]:
        """
        Generates a list of all expected repayments within a given date range.
        """
        if self.credit_type == 'planned':
            return [(d, m) for d, m in self.schedule if start_date <= d <= end_date]
        return []

    def summary(self) -> str:
        """Return a formatted summary of the credit."""
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Debtor: {self.debtor}",
            f"- Type: {self.credit_type}",
            f"- Principal: {self.principal} at {self.interest_rate*100:.2f}% p.a.",
            f"- Origination Date: {self.origination_date}",
            f"- Certainty: {self.certainty:.1%}",
        ]
        
        if self.credit_type == 'planned' and self.schedule:
             lines.append("- Repayment Schedule:")
             for d, m in self.schedule:
                 lines.append(f"    * {d}: {m}")
        
        lines.append(f"- Total Outstanding (Full Amount): {self.total_outstanding()}")
        lines.append(f"- Expected Value (for Net Worth): {self.expected_value()}")
        
        return "\n".join(lines)


# --- Example Usage ---
if __name__ == '__main__':
    today = date(2025, 7, 26)

    # 1. Example of a standard, certain loan
    print("--- Example 1: Standard Loan (100% Certainty) ---")
    standard_loan = Credit(
        debtor='Alice (Family)',
        principal=Money(1000, 'USD'),
        credit_type='planned',
        repayment_schedule=[(today + relativedelta(days=+90), Money(1000, 'USD'))],
        origination_date=today,
        certainty=1.0
    )
    print(standard_loan.summary())

    print("\n" + "="*50 + "\n")

    # 2. Example of an uncertain, risky loan
    print("--- Example 2: Risky Loan (60% Certainty) ---")
    risky_loan = Credit(
        debtor='Startup Inc.',
        principal=Money(5000, 'EUR'),
        credit_type='planned',
        interest_rate=0.08,
        repayment_schedule=[(today + relativedelta(years=+1), Money(5400, 'EUR'))],
        origination_date=today,
        certainty=0.60 # Only 60% confident of getting this back
    )
    print(risky_loan.summary())