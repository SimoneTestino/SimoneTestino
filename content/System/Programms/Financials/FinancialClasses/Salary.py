#!/usr/bin/env python3
"""
Salary.py

Represents a recurring income stream like a salary, which does not contribute
to current net worth but can be used for cashflow forecasting. Includes optional
details for hourly pay and time commitment.
"""

from datetime import date
from typing import List, Tuple, Optional, Literal
from decimal import Decimal
from moneyed import Money
from dateutil.relativedelta import relativedelta

Frequency = Literal['weekly', 'monthly', 'annually']

class Salary:
    """
    Represents a recurring income stream (e.g., salary from an employer).

    A Salary's value for net worth calculations is always zero. It is used for
    forecasting future cashflow and comparing jobs based on hourly rates and
    time commitment.
    """
    def __init__(
        self,
        employer: str,
        payment: Money,
        frequency: Frequency = 'monthly',
        start_date: Optional[date] = None,
        annual_growth_rate: float = 0.0,
        end_date: Optional[date] = None,
        pay_per_hour: Optional[Money] = None,
        weekly_hours: Optional[float] = None
    ):
        self.name = f"Salary from {employer}"
        self.asset_class = 'income_stream'
        self.employer = employer
        self.payment = payment
        self.frequency = frequency
        self.start_date = start_date or date.today()
        self.annual_growth_rate = annual_growth_rate
        self.end_date = end_date
        self.pay_per_hour = pay_per_hour
        self.weekly_hours = weekly_hours

    def get_value_for_net_worth(self, on_date: Optional[date] = None) -> Money:
        """
        Returns the value of the salary for net worth calculation, which is always zero.
        """
        return Money(0, self.payment.currency)

    def generate_cashflow_schedule(self, start_date: date, end_date: date) -> List[Tuple[date, Money]]:
        """
        Generates a list of all expected salary payments within a given date range.
        """
        generated_schedule = []
        
        current_date = self.start_date
        # Find the first payment date on or after the schedule's start date
        while current_date < start_date:
            if self.frequency == 'weekly':
                current_date += relativedelta(weeks=+1)
            elif self.frequency == 'monthly':
                current_date += relativedelta(months=+1)
            else: # annually
                current_date += relativedelta(years=+1)
        
        final_date = min(end_date, self.end_date) if self.end_date else end_date

        while current_date <= final_date:
            years_passed = (current_date - self.start_date).days / 365.25
            growth_factor = (Decimal('1') + Decimal(str(self.annual_growth_rate))) ** Decimal(str(years_passed))
            current_payment = self.payment * growth_factor
            
            generated_schedule.append((current_date, current_payment))

            if self.frequency == 'weekly':
                current_date += relativedelta(weeks=+1)
            elif self.frequency == 'monthly':
                current_date += relativedelta(months=+1)
            else:
                current_date += relativedelta(years=+1)

        return generated_schedule

    def summary(self) -> str:
        """Returns a formatted summary of the salary."""
        lines = [
            f"{self.name} [{self.asset_class}]",
            f"- Employer: {self.employer}",
            f"- Payment: {self.payment} per {self.frequency}",
        ]
        if self.pay_per_hour:
            lines.append(f"- Hourly Rate: {self.pay_per_hour}")
        if self.weekly_hours:
            lines.append(f"- Time Commitment: {self.weekly_hours} hours/week")
        
        lines.append(f"- Annual Growth: {self.annual_growth_rate:.2%}")
        lines.append(f"- Start Date: {self.start_date}")
        if self.end_date:
            lines.append(f"- Expected End Date: {self.end_date}")
        
        return "\n".join(lines)


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Example of a standard monthly salary
    main_job = Salary(
        employer="Tech Corp",
        payment=Money(4000, "EUR"),
        frequency='monthly',
        start_date=date(2024, 1, 1),
        annual_growth_rate=0.03,
        end_date=date(2044, 1, 1),
        weekly_hours=40 # No hourly rate provided
    )
    print("--- Example 1: Standard Monthly Salary ---")
    print(main_job.summary())
    
    print("\n" + "="*50 + "\n")
    
    # 2. Example of a weekly freelance job with full details
    freelance_work = Salary(
        employer="Myself (Freelance)",
        payment=Money(300, "EUR"), # The weekly payment
        frequency='weekly',
        start_date=date(2025, 1, 1),
        pay_per_hour=Money(30, "EUR"), # Explicitly set hourly rate
        weekly_hours=10
    )
    print("--- Example 2: Weekly Freelance Work ---")
    print(freelance_work.summary())

    # 3. Generate cashflow for the freelance work
    print("\n--- Expected Cashflow for Feb 2025 (Freelance) ---")
    cashflow_freelance = freelance_work.generate_cashflow_schedule(
        start_date=date(2025, 2, 1),
        end_date=date(2025, 2, 28)
    )
    for d, p in cashflow_freelance:
        print(f"  {d}: {p}")