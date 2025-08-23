#!/usr/bin/env python3
"""
UrbeProperty.py

This file defines and instantiates all the components for the Casa Urbe property,
populating a Register object with the apartments, rooms, and initial guest booking.
"""
from datetime import date
from moneyed import Money
# --- Path Setup ---
import sys
import os

# This block allows the script to find other project folders
current_dir = os.path.dirname(os.path.abspath(__file__))
coliving_dir = os.path.dirname(current_dir)
project_root = os.path.dirname(coliving_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# --- END ---

# --- Imports ---
from ColivingLiguria.RegisterClasses.Room import Bedroom, Kitchen, Bathroom
from ColivingLiguria.RegisterClasses.Apartment import Apartment
from ColivingLiguria.RegisterClasses.Register import Register
from ColivingLiguria.RegisterClasses.Guest import Guest

# --- Main Data Definition ---
today = date(2025, 8, 23)

# --- Shared Details for the Property ---
shared_garden_details = {
    'size': 400,
    'shared': True,
    'shared_with': 'All apartments in Casa Urbe'
}
wifi_details = {
    'type': 'Mobile Data',
    'mobile_type': '5G',
    'speed_history': [(today, 60.0, 5.0)]
}
stairs_to_apt_3 = {'type': 'external', 'connects_to': 'Apartment 3'}
stairs_to_apt_1 = {'type': 'external', 'connects_to': 'Apartment 1'}

# --- Apartment 1 (Ground Floor - Under Renovation) ---
apt1_kitchen = Kitchen(name="Apt. 1 Kitchen", square_meters=20, has_fridge=True, has_hob=False, has_oven=False)
apt1_bathroom = Bathroom(name="Apt. 1 Bathroom", square_meters=6)
apt1_bedroom_A = Bedroom(
    name="Apt. 1 - Room A",
    square_meters=12, # Corrected size
    sleeping_places=2,
    price_history=[(today, Money(0, "EUR"))],
    legal_capacity=2,
    actual_capacity=3,
    average_ceiling_height=2.7,
    kitchen=apt1_kitchen,
    bathroom=apt1_bathroom,
    allows_pets=False
)
apt1_bedroom_B = Bedroom(
    name="Apt. 1 - Room B",
    square_meters=12, # Corrected size
    sleeping_places=2,
    price_history=[(today, Money(0, "EUR"))],
    legal_capacity=2,
    actual_capacity=3,
    average_ceiling_height=2.7,
    kitchen=apt1_kitchen,
    bathroom=apt1_bathroom,
    allows_pets=False
)
apartment_1 = Apartment(
    name="Apartment 1 (Ground Floor)",
    components=[apt1_kitchen, apt1_bathroom, apt1_bedroom_A, apt1_bedroom_B],
    address="Via Vara Superiore, 86, Urbe, Savona",
    dati_catastali="TBD",
    ownership="managed",
    total_square_meters=50,
    energy_class="G",
    has_double_glazing=False,
    garden_details=shared_garden_details,
    wifi_details=wifi_details,
    stairs_connection=stairs_to_apt_3
)

# --- Apartment 3 (First Floor - Available) ---
apt3_kitchen = Kitchen(name="Apt. 3 Kitchen", square_meters=20, has_fridge=True, has_hob=False, has_oven=False)
apt3_bathroom = Bathroom(name="Apt. 3 Bathroom", square_meters=6)
apt3_bedroom_terrace = Bedroom(
    name="Apt. 3 - Room with Terrace",
    square_meters=12, # Corrected size
    sleeping_places=2,
    price_history=[(today, Money(400, "EUR"))],
    legal_capacity=2,
    actual_capacity=3,
    average_ceiling_height=2.7,
    kitchen=apt3_kitchen,
    bathroom=apt3_bathroom,
    has_terrace=True,
    allows_pets=True # Updated to allow pets
)
apt3_bedroom_no_terrace = Bedroom(
    name="Apt. 3 - Standard Room",
    square_meters=12, # Corrected size
    sleeping_places=2,
    price_history=[(today, Money(350, "EUR"))],
    legal_capacity=2,
    actual_capacity=3,
    average_ceiling_height=2.7,
    kitchen=apt3_kitchen,
    bathroom=apt3_bathroom,
    allows_pets=False
)
apartment_3 = Apartment(
    name="Apartment 3 (First Floor)",
    components=[apt3_kitchen, apt3_bathroom, apt3_bedroom_terrace, apt3_bedroom_no_terrace],
    address="Via Vara Superiore, 86, Urbe, Savona",
    dati_catastali="TBD",
    ownership="managed",
    total_square_meters=50,
    energy_class="G",
    has_double_glazing=False,
    garden_details=shared_garden_details,
    wifi_details=wifi_details,
    stairs_connection=stairs_to_apt_1
)

# --- Main Register Setup ---
urbe_register = Register(name="Casa Urbe Register")
urbe_register.add_apartment(apartment_1)
urbe_register.add_apartment(apartment_3)

# --- Add Initial Guest and Booking ---
# 1. Create the guest
first_guest = Guest(
    name="Maria Rossi",
    id_code="IT-MR12345",
    nationality="Italian",
    age=25,
    pets={'dog': 1} # She is coming with a dog
)
urbe_register.add_guest(first_guest)

# 2. Create the booking for the guest
urbe_register.create_booking(
    guest=first_guest,
    apartment=apartment_3,
    room=apt3_bedroom_terrace,
    check_in_date=date(2025, 9, 1),
    check_out_date=date(2025, 10, 31),
    payment_amount=Money(400, "EUR"), # This is the rent
    payment_type='per_period',
    payment_frequency='monthly',
    deposit=Money(400, "EUR"),
    deposit_paid=True # The deposit has been paid
)

# --- Example Printout ---
if __name__ == "__main__":
    print("--- Casa Urbe Register Summary ---")
    urbe_register.summary()

    print("\n--- Guest Details ---")
    print(first_guest.summary())