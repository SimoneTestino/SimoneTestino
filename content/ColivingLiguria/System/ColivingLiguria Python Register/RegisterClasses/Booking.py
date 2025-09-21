#!/usr/bin/env python3
"""
Booking.py

Defines the Booking class, which represents the contractual details of a
guest's stay, with enhanced payment tracking functionalities.
"""
from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Tuple, Optional, Literal, TYPE_CHECKING
from moneyed import Money, EUR
from dateutil.relativedelta import relativedelta
from decimal import Decimal

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- Type Hint Imports ---
if TYPE_CHECKING:
    from .Guest import Guest
    from .Apartment import Apartment
    from .Room import Bedroom

# --- Type Definitions ---
PaymentType = Literal['per_period', 'total_period']
PaymentFrequency = Literal['nightly', 'weekly', 'monthly']
RoomType = Literal['private', 'shared']

class Booking:
    """
    Represents a single booking with detailed payment and balance tracking.
    All monetary values must be in EUR.
    """
    def __init__(
        self,
        guest: "Guest",
        apartment: "Apartment",
        room: "Bedroom",
        check_in_date: date,
        check_out_date: date,
        payment_amount: Money,
        payment_type: PaymentType,
        payment_frequency: Optional[PaymentFrequency] = None,
        deposit: Optional[Money] = None,
        booking_fee: Optional[Money] = None,
        rating: Optional[float] = None,
        room_type: RoomType = 'private',
        shared_with: Optional[List["Guest"]] = None,
        # --- NEW: More detailed payment attributes ---
        deposit_payment_date: Optional[date] = None,
        fee_payment_date: Optional[date] = None,
        rent_payments: Optional[List[Tuple[date, Money]]] = None
    ):
        if payment_type == 'per_period' and not payment_frequency:
            raise ValueError("'payment_frequency' must be provided for 'per_period' payments.")
        if payment_amount.currency.code != 'EUR': raise ValueError("Payment amount must be in EUR.")
        if deposit and deposit.currency.code != 'EUR': raise ValueError("Deposit must be in EUR.")
        if booking_fee and booking_fee.currency.code != 'EUR': raise ValueError("Booking fee must be in EUR.")

        self.guest = guest
        self.apartment = apartment
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.payment_amount = payment_amount
        self.payment_type = payment_type
        self.payment_frequency = payment_frequency
        self.deposit = deposit
        self.booking_fee = booking_fee
        self.rating = rating
        self.room_type = room_type
        self.shared_with = shared_with or []

        # Store payment details
        self.deposit_payment_date = deposit_payment_date
        self.fee_payment_date = fee_payment_date
        self.rent_payments = rent_payments or []

    # --- NEW: Properties for easy status checks ---
    @property
    def is_deposit_paid(self) -> bool:
        return self.deposit_payment_date is not None

    @property
    def is_fee_paid(self) -> bool:
        return self.fee_payment_date is not None

    @property
    def total_rent_paid(self) -> Money:
        if not self.rent_payments:
            return Money(0, EUR)
        return sum((p[1] for p in self.rent_payments), Money(0, EUR))

    @property
    def outstanding_rent_balance(self) -> Money:
        return self.get_total_rent_due() - self.total_rent_paid

    # --- NEW: Methods to manage payments ---
    def mark_deposit_as_paid(self, payment_date: Optional[date] = None):
        self.deposit_payment_date = payment_date or date.today()
        print(f"Deposit of {self.deposit} for {self.guest.name}'s booking marked as paid on {self.deposit_payment_date}.")

    def record_rent_payment(self, amount: Money, payment_date: Optional[date] = None):
        if amount.currency.code != 'EUR': raise ValueError("Payment must be in EUR.")
        payment_date = payment_date or date.today()
        self.rent_payments.append((payment_date, amount))
        print(f"Recorded rent payment of {amount} for {self.guest.name} on {payment_date}.")

    # --- NEW: Calculation for total expected rent ---
    def get_total_rent_due(self) -> Money:
        if self.payment_type == 'total_period':
            return self.payment_amount

        if self.payment_type == 'per_period':
            periods = 0
            if self.payment_frequency == 'monthly':
                # Calculate the number of full months between dates
                delta = relativedelta(self.check_out_date, self.check_in_date)
                periods = delta.years * 12 + delta.months
                if delta.days > 0: periods += 1 # Count partial months as a full period
            elif self.payment_frequency == 'weekly':
                periods = Decimal((self.check_out_date - self.check_in_date).days / 7).to_integral_value()
            elif self.payment_frequency == 'nightly':
                periods = (self.check_out_date - self.check_in_date).days
            
            return self.payment_amount * periods
        return Money(0, EUR)

    def summary(self) -> str:
        # --- UPDATED: Summary now shows detailed financial status ---
        lines = [
            f"Booking for {self.guest.name} from {self.check_in_date} to {self.check_out_date}",
            f"- Room: {getattr(self.room, 'name', 'N/A')} ({self.room_type})",
        ]

        if self.deposit:
            status = f"(Paid on {self.deposit_payment_date})" if self.is_deposit_paid else "(Outstanding)"
            lines.append(f"- Deposit: {self.deposit} {status}")
        
        if self.booking_fee:
            status = f"(Paid on {self.fee_payment_date})" if self.is_fee_paid else "(Outstanding)"
            lines.append(f"- Booking Fee: {self.booking_fee} {status}")

        total_due = self.get_total_rent_due()
        total_paid = self.total_rent_paid
        outstanding = self.outstanding_rent_balance
        lines.append(f"- Rent: {total_due} (Paid: {total_paid}, Outstanding: {outstanding})")
        if self.rent_payments:
            lines.append("  - Payments Received:")
            for p_date, p_amount in self.rent_payments:
                lines.append(f"    * {p_amount} on {p_date}")
        
        return "\n".join(lines)