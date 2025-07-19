from datetime import date
from typing import List, Tuple, Optional, Literal
from decimal import Decimal
from moneyed import Money, get_currency
from forex_python.converter import CurrencyRates
import warnings

DebitType = Literal['planned', 'conditional']

class Debit:
    """
    Represents an obligation you owe to a creditor, with optional repayment scheduling.

    Attributes:
      - creditor: entity owed
      - principal: negative Money amount owed
      - debit_type: 'planned' or 'conditional'
      - interest_rate: annual rate (e.g. 0.05 for 5%)
      - schedule: list of (date, Money) negative payments (only for 'planned')
    """
    def __init__(
        self,
        creditor: str,
        principal: Money,
        debit_type: DebitType = 'planned',
        interest_rate: float = 0.0,
        repayment_schedule: Optional[List[Tuple[date, Money]]] = None
    ):
        self.creditor = creditor
        self.name = f"Debit to {creditor}"
        self.asset_class = 'debit'
        # Ensure principal is stored negative
        amt = Decimal(principal.amount)
        if amt > 0:
            amt = -amt
        self.principal = Money(amt, principal.currency)

        self.debit_type = debit_type
        self.interest_rate = interest_rate
        self._fx = CurrencyRates()

        # Only planned debits use a schedule
        self.schedule: List[Tuple[date, Money]] = []
        if self.debit_type == 'planned':
            if not repayment_schedule:
                warnings.warn("Planned debit without a repayment schedule.")
            else:
                # Store schedule amounts as negative
                for dt, m in repayment_schedule:
                    m_amt = Decimal(m.amount)
                    if m_amt > 0:
                        m_amt = -m_amt
                    self.schedule.append((dt, Money(m_amt, m.currency)))
            # Validate sum equals principal + interest
            if self.schedule:
                last_date = max(dt for dt, _ in self.schedule)
                days = (last_date - date.today()).days
                rate = Decimal(str(self.interest_rate))
                expected = Decimal(self.principal.amount) * (Decimal('1') + rate * Decimal(days) / Decimal('365'))
                total_sched = sum(m.amount for _, m in self.schedule)
                if abs(total_sched - expected) > Decimal('1e-8'):
                    warnings.warn(
                        f"Schedule total ({total_sched}) does not match owed ({expected})."
                    )
        else:
            # conditional: ignore schedule
            if repayment_schedule:
                warnings.warn("Conditional debit provided schedule; ignoring.")

    def total_scheduled(self) -> Money:
        """
        Sum of scheduled repayments (negative), only for 'planned'.
        """
        if self.debit_type != 'planned':
            warnings.warn("total_scheduled() only applies to planned debits.")
            return Money(Decimal('0'), self.principal.currency)
        total = sum(m.amount for _, m in self.schedule)
        return Money(total, self.principal.currency)

    def total_outstanding(self) -> Money:
        """
        Remaining owed including pro rata interest.
        For planned: principal + interest to today minus paid.
        For conditional: principal + interest to today.
        """
        today = date.today()
        rate = Decimal(str(self.interest_rate))
        days = Decimal((today - today).days)  # zero
        # interest on principal from today: zero
        base = Decimal(self.principal.amount)
        interest_amt = base * rate * days / Decimal('365')
        owed = base + interest_amt
        if self.debit_type == 'planned' and self.schedule:
            paid = sum(m.amount for d, m in self.schedule if d <= today)
            owed = owed - paid
        return Money(owed, self.principal.currency)

    def is_fully_scheduled(self) -> bool:
        """
        True if planned schedule covers full owed amount including interest.
        """
        if self.debit_type != 'planned':
            return False
        if not self.schedule:
            return False
        last_date = max(d for d, _ in self.schedule)
        days = (last_date - date.today()).days
        expected = Decimal(self.principal.amount) * (Decimal('1') + Decimal(str(self.interest_rate)) * Decimal(days) / Decimal('365'))
        total_sched = sum(m.amount for _, m in self.schedule)
        return abs(total_sched - expected) < Decimal('1e-8')

    def convert_to(self, target_currency: str) -> Money:
        """
        Convert outstanding owed to another currency.
        """
        src = self.principal.currency.code
        tgt = target_currency.upper()
        rate = self._fx.get_rate(src, tgt)
        amt = Decimal(str(self.total_outstanding().amount)) * Decimal(str(rate))
        return Money(amt, get_currency(tgt))

    def summary(self) -> str:
        """
        Return formatted summary.
        """
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Method: {self.debit_type}",
            f"- Principal: {self.principal} at {self.interest_rate*100:.2f}% p.a.",
            f"- Creditor: {self.creditor}"
        ]
        if self.debit_type == 'planned':
            lines.append("- Schedule:")
            for d, m in self.schedule:
                lines.append(f"    * {d}: {m}")
            lines.append(f"- Total Scheduled: {self.total_scheduled()}")
            lines.append(f"- Fully Scheduled: {self.is_fully_scheduled()}")
        lines.append(f"- Outstanding: {self.total_outstanding()}")
        return "\n".join(lines)

# Example
if __name__ == '__main__':
    sched = [
        (date(2025,5,1), Money(200, get_currency('USD'))),
        (date(2025,8,1), Money(300, get_currency('USD')))
    ]
    planned = Debit('Bank', Money(500, get_currency('USD')), 'planned', 0.05, sched)
    print(planned.summary())
    cond = Debit('Partner', Money(1000, get_currency('EUR')), 'conditional', 0.03)
    print(cond.summary())