#!/usr/bin/env python3
"""
Register.py

Defines the main Register class that manages all apartments, rooms, guests,
and bookings, including conflict detection.
"""

from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Optional, Dict

# --- ROBUST PATH SETUP AND IMPORTS ---
# This block makes the script runnable on its own.
# You can copy this entire block to the top of your other files in this folder.
try:
    # This works when run from a main script
    from ColivingLiguria.RegisterClasses.Apartment import Apartment
    from ColivingLiguria.RegisterClasses.Room import Bedroom, Kitchen, Bathroom
    from ColivingLiguria.RegisterClasses.Guest import Guest, Booking
    from moneyed import Money
except ImportError:
    # This works when the script is run directly
    current_dir = os.path.dirname(os.path.abspath(__file__))
    coliving_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(coliving_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from ColivingLiguria.RegisterClasses.Apartment import Apartment
    from ColivingLiguria.RegisterClasses.Room import Bedroom, Kitchen, Bathroom
    from ColivingLiguria.RegisterClasses.Guest import Guest, Booking
    from moneyed import Money
# --- END OF BLOCK ---


class Register:
    """
    The central register for managing properties, guests, and bookings.
    """
    def __init__(self, name: str):
        self.name = name
        self.apartments: List[Apartment] = []
        self.guests: List[Guest] = []
        self.bookings: List[Booking] = []

    def add_apartment(self, apartment: Apartment):
        """Adds a new apartment to the register."""
        self.apartments.append(apartment)

    def add_guest(self, guest: Guest):
        """Adds a new guest to the register."""
        self.guests.append(guest)

    def _check_for_booking_conflicts(self, room: Bedroom, check_in: date, check_out: date) -> bool:
        """
        Checks if a new booking for a specific room and date range would cause a conflict.
        """
        bookings_for_room = [b for b in self.bookings if b.room.name == room.name]

        for existing_booking in bookings_for_room:
            if check_in < existing_booking.check_out_date and check_out > existing_booking.check_in_date:
                if existing_booking.room_type == 'private':
                    print(f"!! CONFLICT: Room '{room.name}' is already booked as private from "
                          f"{existing_booking.check_in_date} to {existing_booking.check_out_date}.")
                    return True
        return False

    def create_booking(self, guest: Guest, apartment: Apartment, room: Bedroom, **kwargs) -> Optional[Booking]:
        """
        Creates a new booking after checking for conflicts.
        """
        print(f"\nAttempting to create booking for {guest.name} in '{room.name}'...")
        
        check_in = kwargs.get('check_in_date')
        check_out = kwargs.get('check_out_date')

        if not (check_in and check_out):
            print("!! ERROR: Booking requires a check_in_date and check_out_date.")
            return None

        if self._check_for_booking_conflicts(room, check_in, check_out):
            print("-> Booking failed due to a conflict.")
            return None
        
        new_booking = guest.add_booking(apartment=apartment, room=room, **kwargs)
        self.bookings.append(new_booking)
        print("-> Booking confirmed successfully.")
        return new_booking

    def get_occupancy_on_date(self, target_date: date) -> Dict[str, List[str]]:
        """Returns a dictionary of which guests are in which rooms on a given date."""
        occupancy = {}
        for booking in self.bookings:
            if booking.check_in_date <= target_date < booking.check_out_date:
                room_name = getattr(booking.room, 'name', 'Unknown Room')
                if room_name not in occupancy:
                    occupancy[room_name] = []
                occupancy[room_name].append(booking.guest.name)
        return occupancy

    def summary(self):
        """Prints a high-level summary of the register."""
        print("\n" + "="*30)
        print(f"Register Summary: {self.name}")
        print("="*30)
        print(f"- Total Apartments: {len(self.apartments)}")
        print(f"- Total Guests: {len(self.guests)}")
        print(f"- Total Bookings: {len(self.bookings)}")
        
        print("\n--- Current Occupancy ---")
        occupancy_today = self.get_occupancy_on_date(date.today())
        if not occupancy_today:
            print("No guests currently checked in.")
        else:
            for room, guests in occupancy_today.items():
                print(f"- Room '{room}': {', '.join(guests)}")


# --- Example Usage ---
if __name__ == '__main__':
    coliving_register = Register(name="Coliving Liguria Register")
    
    kitchen = Kitchen(name="Main Kitchen", square_meters=20)
    bathroom = Bathroom(name="Shared Bathroom", square_meters=10)
    
    room_private = Bedroom(name="Private Room 'Sole'", square_meters=25, sleeping_places=1, price_history=[(date.today(), Money(350, "EUR"))], kitchen=kitchen, bathroom=bathroom, legal_capacity=1, actual_capacity=1, average_ceiling_height=2.8)
    
    villa = Apartment(name="Main Villa", components=[kitchen, bathroom, room_private], address="...", dati_catastali="...", ownership='owned')
    coliving_register.add_apartment(villa)

    guest_anna = Guest(name="Anna", id_code="DE123", nationality="German", age=21)
    guest_ben = Guest(name="Ben", id_code="US456", nationality="American", age=23)
    coliving_register.add_guest(guest_anna)
    coliving_register.add_guest(guest_ben)

    coliving_register.create_booking(
        guest=guest_anna, apartment=villa, room=room_private,
        check_in_date=date(2025, 9, 1), check_out_date=date(2025, 10, 31),
        payment_amount=Money(400, "EUR"), payment_type='per_period',
        payment_frequency='monthly', room_type='private'
    )
    
    coliving_register.create_booking(
        guest=guest_ben, apartment=villa, room=room_private,
        check_in_date=date(2025, 10, 15), check_out_date=date(2025, 11, 15),
        payment_amount=Money(400, "EUR"), payment_type='per_period',
        payment_frequency='monthly', room_type='private'
    )

    coliving_register.summary()