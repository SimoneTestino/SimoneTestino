#!/usr/bin/env python3
"""
Debit.py
Represents an obligation you owe to a creditor, using the central CurrencyConverter.
"""

from datetime import date
from typing import List, Tuple, Optional, Literal
from decimal import Decimal
from moneyed import Money
import warnings

from Helper.CurrencyConverter import CurrencyConverter

DebitType = Literal['planned', 'conditional']

class Debit:
    """
    Represents an obligation you owe to a creditor.
    """
    def __init__(
        self,
        creditor: str,
        principal: Money,
        debit_type: DebitType = 'planned',
        interest_rate: float = 0.0,
        repayment_schedule: Optional[List[Tuple[date, Money]]] = None,
        origination_date: Optional[date] = None
    ):
        self.creditor = creditor
        self.name = f"Debit to {creditor}"
        self.asset_class = 'debit'
        
        amt = abs(Decimal(principal.amount)) * -1
        self.principal = Money(amt, principal.currency)

        self.debit_type = debit_type
        self.interest_rate = interest_rate
        self.origination_date = origination_date or date.today()
        self._converter = CurrencyConverter()

        self.schedule: List[Tuple[date, Money]] = []
        if self.debit_type == 'planned' and repayment_schedule:
            for dt, m in repayment_schedule:
                m_amt = abs(Decimal(m.amount)) * -1
                self.schedule.append((dt, Money(m_amt, m.currency)))
            self.schedule.sort()
        # NOTE: Automatic validation has been removed to reduce unnecessary warnings.
        # Use the .is_fully_scheduled() method for manual checks.

    def total_scheduled(self) -> Money:
        """Sum of scheduled repayments (negative), only for 'planned' debits."""
        if self.debit_type != 'planned':
            return Money(Decimal('0'), self.principal.currency)
        return Money(sum(m.amount for _, m in self.schedule), self.principal.currency)

    def total_outstanding(self, on_date: Optional[date] = None) -> Money:
        """Calculates remaining owed including pro rata simple interest."""
        valuation_date = on_date or date.today()
        if valuation_date < self.origination_date:
            return self.principal

        rate = Decimal(str(self.interest_rate))
        base = self.principal.amount
        days = (valuation_date - self.origination_date).days
        interest_to_date = base * rate * Decimal(days) / Decimal('365')
        total_owed = base + interest_to_date

        if self.debit_type == 'planned' and self.schedule:
            paid_amount = sum(p.amount for d, p in self.schedule if d <= valuation_date)
            total_owed -= paid_amount
            
        return Money(total_owed, self.principal.currency)

    def is_fully_scheduled(self) -> bool:
        """
        True if the planned schedule is within 10% of the simple interest expectation.
        """
        if self.debit_type != 'planned' or not self.schedule:
            return False
            
        last_date = self.schedule[-1][0]
        days = (last_date - self.origination_date).days
        rate = Decimal(str(self.interest_rate))
        expected = self.principal.amount * (Decimal('1') + rate * Decimal(days) / Decimal('365'))
        total_sched = sum(m.amount for _, m in self.schedule)
        
        if abs(expected) == 0:
            return abs(total_sched) == 0
        
        difference_pct = abs((total_sched - expected) / expected)
        return difference_pct <= Decimal('0.10')

    def convert_to(self, target_currency: str) -> Money:
        """Converts the outstanding owed amount to another currency."""
        outstanding_money = self.total_outstanding()
        return self._converter.convert(outstanding_money, target_currency)

    def summary(self) -> str:
        """Return a formatted summary of the debit."""
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Creditor: {self.creditor}",
            f"- Type: {self.debit_type}",
            f"- Principal: {self.principal} at {self.interest_rate*100:.2f}% p.a.",
            f"- Origination Date: {self.origination_date}",
        ]
        if self.debit_type == 'planned':
            lines.append("- Repayment Schedule:")
            for d, m in self.schedule:
                lines.append(f"    * {d}: {m}")
            lines.append(f"- Is Fully Scheduled (within 10%): {self.is_fully_scheduled()}")
        
        lines.append(f"- Outstanding as of {date.today()}: {self.total_outstanding()}")
        return "\n".join(lines)

# --- Example Usage ---
if __name__ == '__main__':
    from datetime import timedelta

    loan_start = date.today() - timedelta(days=30)
    loan_schedule = [
        (loan_start + timedelta(days=60), Money(255, 'EUR')),
        (loan_start + timedelta(days=120), Money(255, 'EUR'))
    ]

    my_loan = Debit(
        creditor="My Bank",
        principal=Money(500, "EUR"),
        interest_rate=0.05,
        repayment_schedule=loan_schedule,
        origination_date=loan_start
    )

    print(my_loan.summary())