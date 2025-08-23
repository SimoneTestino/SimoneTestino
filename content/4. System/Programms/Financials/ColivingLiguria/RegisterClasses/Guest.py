#!/usr/bin/env python3
"""
Guest.py

Defines the Guest and Booking classes to manage guest information and their stays.
"""

# --- FIX: Corrected the typo in the import statement ---
from __future__ import annotations

import sys
import os
from datetime import date
from typing import List, Tuple, Optional, Literal, Dict, Any
from moneyed import Money

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
coliving_dir = os.path.dirname(current_dir)
project_root = os.path.dirname(coliving_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports for type hints and example ---
try:
    from .Apartment import Apartment
    from .Room import Bedroom
except ImportError:
    class Apartment: pass
    class Bedroom: pass

# --- Type Definitions ---
PaymentType = Literal['per_period', 'total_period']
PaymentFrequency = Literal['nightly', 'weekly', 'monthly']
RoomType = Literal['private', 'shared']

class Booking:
    """
    Represents a single booking made by a guest for a specific period and room.
    All monetary values must be in EUR.
    """
    def __init__(
        self,
        guest: Guest,
        apartment: Apartment,
        room: Bedroom,
        check_in_date: date,
        check_out_date: date,
        payment_amount: Money,
        payment_type: PaymentType,
        payment_paid: bool = False,
        payment_frequency: Optional[PaymentFrequency] = None,
        deposit: Optional[Money] = None,
        deposit_paid: bool = False,
        booking_fee: Optional[Money] = None,
        booking_fee_paid: bool = False,
        rating: Optional[float] = None,
        room_type: RoomType = 'private',
        shared_with: Optional[List[Guest]] = None
    ):
        if payment_type == 'per_period' and not payment_frequency:
            raise ValueError("'payment_frequency' must be provided for 'per_period' payments.")
        if payment_amount.currency.code != 'EUR':
            raise ValueError("Payment amount must be in EUR.")
        if deposit and deposit.currency.code != 'EUR':
            raise ValueError("Deposit must be in EUR.")
        if booking_fee and booking_fee.currency.code != 'EUR':
            raise ValueError("Booking fee must be in EUR.")

        self.guest = guest
        self.apartment = apartment
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.payment_amount = payment_amount
        self.payment_type = payment_type
        self.payment_paid = payment_paid
        self.payment_frequency = payment_frequency
        self.deposit = deposit
        self.deposit_paid = deposit_paid
        self.booking_fee = booking_fee
        self.booking_fee_paid = booking_fee_paid
        self.rating = rating
        self.room_type = room_type
        self.shared_with = shared_with or []

    def summary(self) -> str:
        payment_desc = f"{self.payment_amount}"
        if self.payment_type == 'per_period':
            payment_desc += f" per {self.payment_frequency}"
        else:
            payment_desc += " for the whole period"
        
        payment_status = "(Paid)" if self.payment_paid else "(Unpaid)"
        deposit_status = "(Paid)" if self.deposit_paid else "(Unpaid)"
        fee_status = "(Paid)" if self.booking_fee_paid else "(Unpaid)"

        lines = [
            f"Booking from {self.check_in_date} to {self.check_out_date}",
            f"- Apartment: {getattr(self.apartment, 'name', 'N/A')}",
            f"- Room: {getattr(self.room, 'name', 'N/A')} ({self.room_type})",
            f"- Payment: {payment_desc} {payment_status}",
        ]
        if self.deposit: lines.append(f"- Deposit: {self.deposit} {deposit_status}")
        if self.booking_fee: lines.append(f"- Booking Fee: {self.booking_fee} {fee_status}")
        if self.shared_with:
            roommates = ", ".join([g.name for g in self.shared_with])
            lines.append(f"- Shared With: {roommates}")
        if self.rating: lines.append(f"- Guest Rating: {self.rating} / 5.0")
        
        return "\n".join(lines)


class Guest:
    """
    Represents a guest, containing their personal information and a history of their bookings.
    """
    def __init__(
        self,
        name: str,
        id_code: str,
        nationality: str,
        age: int,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        gender: Optional[str] = None,
        is_volunteer: bool = False,
        pets: Optional[Dict[str, int]] = None,
        arrived_independently: bool = True
    ):
        self.name = name
        self.id_code = id_code
        self.nationality = nationality
        self.age = age
        self.email = email
        self.phone = phone
        self.gender = gender
        self.is_volunteer = is_volunteer
        self.pets = pets or {}
        self.arrived_independently = arrived_independently
        self.bookings: List[Booking] = []

    def add_booking(self, **kwargs) -> Booking:
        booking = Booking(guest=self, **kwargs)
        self.bookings.append(booking)
        self.bookings.sort(key=lambda b: b.check_in_date)
        return booking

    def summary(self) -> str:
        lines = [
            f"Guest Summary: {self.name}",
            f"- ID: {self.id_code}, Nationality: {self.nationality}, Age: {self.age}",
            f"- Contact: {self.email or 'N/A'}",
            f"- Volunteer: {'Yes' if self.is_volunteer else 'No'}",
        ]
        if self.pets:
            pet_list = ", ".join([f"{count} {animal}" for animal, count in self.pets.items() if count > 0])
            lines.append(f"- Pets: {pet_list}")

        lines.append("\n--- Bookings ---")
        if not self.bookings:
            lines.append("  No bookings on record.")
        else:
            for booking in self.bookings:
                lines.append(booking.summary().replace("\n", "\n  "))
        
        return "\n".join(lines)


# --- Example Usage ---
if __name__ == "__main__":
    class MockApartment:
        def __init__(self, name): self.name = name
    class MockBedroom:
        def __init__(self, name): self.name = name
    
    villa = MockApartment("Villa 'La Quiete'")
    room1 = MockBedroom("Room 101")
    
    jane_doe = Guest(name="Jane Doe", id_code="AB12345CD", nationality="German", age=22)
    
    jane_doe.add_booking(
        apartment=villa,
        room=room1,
        check_in_date=date(2025, 9, 1),
        check_out_date=date(2026, 6, 30),
        payment_amount=Money(350, "EUR"),
        payment_type='per_period',
        payment_frequency='monthly',
        payment_paid=True,
        deposit=Money(700, "EUR"),
        deposit_paid=True
    )
    
    print(jane_doe.summary())