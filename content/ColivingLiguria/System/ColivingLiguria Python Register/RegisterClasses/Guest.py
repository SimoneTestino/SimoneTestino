#!/usr/bin/env python3
"""
Guest.py

Defines the Guest class to manage guest information and their history of bookings.
"""
from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Optional, Dict
from moneyed import Money

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Local Imports ---
# Import the Booking class from its new, separate file.
from Booking import Booking

# --- Class Definition ---
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
        """Creates a new Booking instance and associates it with this guest."""
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
    # Mock classes are needed for the example to run standalone
    class MockApartment:
        def __init__(self, name): self.name = name
    class MockBedroom:
        def __init__(self, name): self.name = name

    villa = MockApartment("Villa 'La Quiete'")
    room1 = MockBedroom("Room 101")

    jane_doe = Guest(name="Jane Doe", id_code="AB12345CD", nationality="German", age=22)

    # The add_booking method now uses the imported Booking class
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