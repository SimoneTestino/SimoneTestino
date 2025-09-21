#!/usr/bin/env python3
"""
Register.py

Defines the main Register class that manages all apartments, rooms, guests,
and bookings, with robust conflict detection and detailed reporting.
"""
from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Optional, Dict

# --- Path Setup ---
# This block makes the script runnable on its own and finds other project modules.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- Imports ---
from Apartment import Apartment
from Room import Room, Bedroom, Kitchen, Bathroom
from Guest import Guest
from Booking import Booking
from moneyed import Money

class Register:
    """
    The central register for managing properties, guests, and bookings.
    """
    def __init__(self, name: str):
        self.name = name
        self.apartments: List[Apartment] = []
        self.guests: List[Guest] = []
        self.bookings: List[Booking] = []
        self.conflict_check_enabled = True # Master switch for conflict checks

    def enable_conflict_check(self, enabled: bool):
        """
        Manually enable or disable booking conflict checks.
        Disabling this can speed up bulk data entry, but risks double-bookings.
        """
        self.conflict_check_enabled = enabled
        status = "ENABLED" if enabled else "DISABLED"
        print(f"-> Booking conflict check is now {status}.")

    def add_apartment(self, apartment: Apartment):
        """Adds a new apartment to the register."""
        self.apartments.append(apartment)

    def add_guest(self, guest: Guest):
        """Adds a new guest to the register."""
        self.guests.append(guest)

    def _check_for_booking_conflicts(self, new_booking_room: Bedroom, new_booking_start: date, new_booking_end: date, new_booking_type: str) -> bool:
        """
        Checks for booking conflicts, handling both private and shared rooms.
        """
        overlapping_bookings = [
            b for b in self.bookings
            if b.room.name == new_booking_room.name and
               (new_booking_start < b.check_out_date and new_booking_end > b.check_in_date)
        ]

        if not overlapping_bookings:
            return False

        for existing in overlapping_bookings:
            if existing.room_type == 'private' or new_booking_type == 'private':
                print(f"!! CONFLICT: Room '{new_booking_room.name}' has a private booking conflict.")
                return True

        num_occupants = len(overlapping_bookings) + 1
        if num_occupants > new_booking_room.actual_capacity:
            print(f"!! CONFLICT: Shared room '{new_booking_room.name}' would exceed capacity.")
            return True

        return False

    def create_booking(self, guest: Guest, apartment: Apartment, room: Bedroom, **kwargs) -> Optional[Booking]:
        """
        Creates a new booking after performing robust conflict checks.
        """
        print(f"\nAttempting to create booking for {guest.name} in '{room.name}'...")
        check_in = kwargs.get('check_in_date')
        check_out = kwargs.get('check_out_date')
        room_type = kwargs.get('room_type', 'private')

        if not (check_in and check_out):
            print("!! ERROR: Booking requires a check_in_date and check_out_date.")
            return None

        # The conflict check is now conditional based on the master switch.
        if self.conflict_check_enabled and self._check_for_booking_conflicts(room, check_in, check_out, room_type):
            print("-> Booking failed due to a conflict.")
            return None

        new_booking = guest.add_booking(apartment=apartment, room=room, **kwargs)
        self.bookings.append(new_booking)
        print(f"-> Booking confirmed successfully for {guest.name}.")
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
        print("\n" + "="*40)
        print(f"Register Summary: {self.name}")
        print("="*40)
        print(f"- Total Apartments: {len(self.apartments)}")
        print(f"- Total Guests: {len(self.guests)}")
        print(f"- Total Bookings: {len(self.bookings)}")

    def print_detailed_report(self):
        """
        Prints a full, structured report of all apartments, guests, and bookings.
        """
        self.summary() # Start with the high-level summary

        print("\n" + "="*40)
        print("DETAILED BOOKING & PROPERTY REPORT")
        print("="*40)

        # 1. Apartment Details
        print("\n--- Apartment Details ---")
        if not self.apartments:
            print("No apartments in the register.")
        else:
            for apt in self.apartments:
                print(f"\n{apt.summary()}")

        # 2. Master Booking List (Chronological)
        print("\n--- All Bookings (Chronological) ---")
        if not self.bookings:
            print("No bookings in the register.")
        else:
            # Sort all bookings by check-in date
            sorted_bookings = sorted(self.bookings, key=lambda b: b.check_in_date)
            for booking in sorted_bookings:
                print(f"\n- Guest: {booking.guest.name}")
                print(f"  Room: {booking.room.name} ({booking.room_type})")
                print(f"  Apartment: {booking.apartment.name}")
                print(f"  Period: {booking.check_in_date} to {booking.check_out_date}")
        print("\n" + "="*40)


# --- Example Usage ---
if __name__ == '__main__':
    register = Register(name="Coliving Liguria Demo")
    kitchen = Kitchen(name="Shared Kitchen", square_meters=20)
    bathroom = Bathroom(name="Shared Bathroom", square_meters=10)
    
    shared_room = Bedroom(
        name="Shared Room 'Tramonto'", square_meters=25, sleeping_places=2,
        price_history=[(date.today(), Money(250, "EUR"))], kitchen=kitchen,
        bathroom=bathroom, legal_capacity=2, actual_capacity=2, average_ceiling_height=2.8
    )
    villa = Apartment(name="Main Villa", components=[kitchen, bathroom, shared_room], address="...", dati_catastali="...", ownership='owned')
    register.add_apartment(villa)

    anna = Guest(name="Anna", id_code="DE123", nationality="German", age=21)
    ben = Guest(name="Ben", id_code="US456", nationality="American", age=23)
    clara = Guest(name="Clara", id_code="FR789", nationality="French", age=25)
    register.add_guest(anna)
    register.add_guest(ben)
    register.add_guest(clara)

    print("\n--- Testing Booking Logic ---")
    
    register.create_booking(guest=anna, apartment=villa, room=shared_room, check_in_date=date(2025, 10, 1), check_out_date=date(2025, 10, 31), payment_amount=Money(250, "EUR"), payment_type='total_period', room_type='shared')
    register.create_booking(guest=ben, apartment=villa, room=shared_room, check_in_date=date(2025, 10, 5), check_out_date=date(2025, 10, 25), payment_amount=Money(250, "EUR"), payment_type='total_period', room_type='shared')
    # This booking should fail because the room's capacity of 2 is exceeded
    register.create_booking(guest=clara, apartment=villa, room=shared_room, check_in_date=date(2025, 10, 10), check_out_date=date(2025, 10, 20), payment_amount=Money(250, "EUR"), payment_type='total_period', room_type='shared')

    print("\n--- Disabling conflict check and re-trying booking ---")
    register.enable_conflict_check(False)
    # This booking will now succeed, even though it creates a conflict
    register.create_booking(guest=clara, apartment=villa, room=shared_room, check_in_date=date(2025, 10, 10), check_out_date=date(2025, 10, 20), payment_amount=Money(250, "EUR"), payment_type='total_period', room_type='shared')
    
    register.enable_conflict_check(True) # Good practice to re-enable it

    # --- DEMONSTRATE NEW REPORTING ---
    register.print_detailed_report()