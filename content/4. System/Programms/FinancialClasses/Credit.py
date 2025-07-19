from datetime import date
from typing import List, Tuple, Optional, Literal
from decimal import Decimal
from moneyed import Money, get_currency
from forex_python.converter import CurrencyRates
import warnings

CreditType = Literal['planned', 'conditional']

class Credit:
    """
    Represents credit extended to a debtor, with optional repayment scheduling.

    Attributes:
      - debtor: entity owing money
      - principal: Money amount lent
      - credit_type: 'planned' or 'conditional'
      - interest_rate: annual rate (e.g. 0.05 for 5%)
      - schedule: list of (date, Money) repayments (only for 'planned')
    """
    def __init__(
        self,
        debtor: str,
        principal: Money,
        credit_type: CreditType = 'planned',
        interest_rate: float = 0.0,
        repayment_schedule: Optional[List[Tuple[date, Money]]] = None
    ):
        self.debtor = debtor
        self.name = f"Credit to {debtor}"
        self.asset_class = 'credit'
        self.principal = principal
        self.credit_type = credit_type
        self.interest_rate = interest_rate
        self._fx = CurrencyRates()

        # Setup schedule for planned credits
        self.schedule: List[Tuple[date, Money]] = []
        if self.credit_type == 'planned':
            if not repayment_schedule:
                warnings.warn("Planned credit without a repayment schedule.")
            else:
                for dt, m in repayment_schedule:
                    # ensure positive repayment amounts
                    amt = Decimal(m.amount)
                    if amt < 0:
                        amt = -amt
                    self.schedule.append((dt, Money(amt, m.currency)))
            # validate total scheduled equals principal+interest
            if self.schedule:
                last_date = max(dt for dt, _ in self.schedule)
                days = (last_date - date.today()).days
                rate = Decimal(str(self.interest_rate))
                expected = Decimal(str(self.principal.amount)) * (Decimal('1') + rate * Decimal(days) / Decimal('365'))
                total_sched = sum(m.amount for _, m in self.schedule)
                if abs(total_sched - expected) > Decimal('1e-8'):
                    warnings.warn(
                        f"Schedule total ({total_sched} {self.principal.currency.code}) "
                        f"does not match expected ({expected} {self.principal.currency.code})."
                    )
        else:
            if repayment_schedule:
                warnings.warn("Conditional credit provided schedule; ignoring.")

    def total_scheduled(self) -> Money:
        """
        Sum of scheduled repayments (only for 'planned').
        """
        if self.credit_type != 'planned':
            warnings.warn("total_scheduled() only applies to planned credits.")
            return Money(Decimal('0'), self.principal.currency)
        total = sum(m.amount for _, m in self.schedule)
        return Money(total, self.principal.currency)

    def total_outstanding(self) -> Money:
        """
        Remaining amount owed to me, including pro rata interest.
        For planned: principal + interest to today minus paid.
        For conditional: principal + interest to today.
        """
        today = date.today()
        rate = Decimal(str(self.interest_rate))
        base = Decimal(str(self.principal.amount))
        # interest accrual since loan date to today
        # assume interest from loan origination (use earliest date)
        start_date = min(d for d, _ in self.schedule) if self.schedule else today
        days = (today - start_date).days
        interest_amt = base * rate * Decimal(days) / Decimal('365')
        owed = base + interest_amt
        if self.credit_type == 'planned' and self.schedule:
            paid = sum(p.amount for d, p in self.schedule if d <= today)
            owed -= paid
        return Money(owed, self.principal.currency)

    def is_fully_scheduled(self) -> bool:
        """
        True if planned schedule covers principal+interest.
        """
        if self.credit_type != 'planned' or not self.schedule:
            return False
        last_date = max(d for d, _ in self.schedule)
        days = (last_date - date.today()).days
        expected = Decimal(str(self.principal.amount)) * (Decimal('1') + Decimal(str(self.interest_rate)) * Decimal(days) / Decimal('365'))
        total_sched = sum(m.amount for _, m in self.schedule)
        return abs(total_sched - expected) < Decimal('1e-8')

    def convert_to(self, target_currency: str) -> Money:
        """
        Convert outstanding credit to another currency.
        """
        src = self.principal.currency.code
        tgt = target_currency.upper()
        rate = self._fx.get_rate(src, tgt)
        return Money(Decimal(str(self.total_outstanding().amount)) * Decimal(str(rate)), get_currency(tgt))

    def summary(self) -> str:
        """
        Return formatted summary.
        """
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Type: {self.credit_type}",
            f"- Principal: {self.principal} at {self.interest_rate*100:.2f}% p.a.",
            f"- Debtor: {self.debtor}"
        ]
        if self.credit_type == 'planned':
            lines.append("- Schedule:")
            for d, m in self.schedule:
                lines.append(f"    * {d}: {m}")
            lines.append(f"- Total Scheduled: {self.total_scheduled()}")
            lines.append(f"- Fully Scheduled: {self.is_fully_scheduled()}")
        lines.append(f"- Outstanding: {self.total_outstanding()}")
        return "\n".join(lines)

# Example usage
if __name__ == '__main__':
    sched = [
        (date(2025,6,1), Money(500, get_currency('USD'))),
        (date(2025,12,1), Money(550, get_currency('USD')))
    ]
    planned = Credit(
        debtor='Alice',
        principal=Money(1000, get_currency('USD')),
        credit_type='planned',
        interest_rate=0.05,
        repayment_schedule=sched
    )
    print(planned.summary())

    cond = Credit(
        debtor='Bob',
        principal=Money(500, get_currency('EUR')),
        credit_type='conditional',
        interest_rate=0.03
    )
    print(cond.summary())