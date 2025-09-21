#!/usr/bin/env python3
"""
ActualData.py

This file defines and instantiates all the components for the Cascina Brignone
property using an efficient, data-driven approach. It populates a register
with all apartments, rooms, guests, and a complex booking schedule.
"""
from datetime import date, timedelta
from moneyed import Money, EUR

# --- ROBUST PATH SETUP ---
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
coliving_dir = os.path.dirname(current_dir)
if coliving_dir not in sys.path:
    sys.path.insert(0, coliving_dir)

# --- Imports ---
from RegisterClasses.Room import Bedroom, Kitchen, Bathroom, OtherRoom
from RegisterClasses.Apartment import Apartment
from RegisterClasses.Register import Register
from RegisterClasses.Guest import Guest
from RegisterClasses.Booking import Booking

# ==============================================================================
# EFFICIENT DATA STRUCTURES
# ==============================================================================
# By defining all data first, we can create objects in an optimized loop.

today = date(2025, 9, 21)
project_start_date = date(2025, 10, 1)
brignone_address = "Località Chiappella 19, Cairo Montenotte, Savona"


PROPERTY_DATA = {
    "Apt. La Noce": {
        "params": {"address": brignone_address, "dati_catastali": "Mappale 519, Subalterno 6", "ownership": "owned", "total_square_meters": 60, "heating_type": "pellet_stove", "remarks": "Designated 'Prima Casa' for tax purposes."},
        "components": [
            {"type": Kitchen, "params": {"name": "La Noce Kitchen", "square_meters": 18, "hob_type": "wood_stove"}},
            {"type": Bathroom, "params": {"name": "La Noce Bathroom", "square_meters": 7, "remarks": "Accessible via external stairs."}},
            {"type": Bedroom, "params": {"name": "Stanza Noce", "square_meters": 16, "sleeping_places": 2, "price_history": [(today, Money(280, "EUR"))], "legal_capacity": 2, "actual_capacity": 2, "allows_pets": True, "average_ceiling_height": 2.7, "remarks": "Private Room"}},
            {"type": Bedroom, "params": {"name": "Stanza Fiume", "square_meters": 14, "sleeping_places": 2, "price_history": [(today, Money(120, "EUR"))], "legal_capacity": 2, "actual_capacity": 2, "allows_pets": True, "average_ceiling_height": 2.7, "remarks": "Shared Room"}}
        ]
    },
    "Apt. Il Rustico": {
        "params": {"address": brignone_address, "dati_catastali": "Mappale 521", "ownership": "owned", "total_square_meters": 50, "heating_type": "wood_stove"},
        "components": [
            {"type": Kitchen, "params": {"name": "Il Rustico Kitchenette", "square_meters": 8, "hob_type": "electric"}},
            {"type": Bathroom, "params": {"name": "Il Rustico Bathroom", "square_meters": 4}},
            {"type": Bedroom, "params": {"name": "Stanza Rustico", "square_meters": 25, "sleeping_places": 2, "price_history": [(today, Money(90, "EUR"))], "legal_capacity": 2, "actual_capacity": 2, "average_ceiling_height": 3.0, "remarks": "Shared Room in converted outbuilding."}}
        ]
    },
    "Apt. Il Forno": {
        "params": {"address": brignone_address, "dati_catastali": "Mappale 440 (Piano Terra)", "ownership": "owned", "total_square_meters": 90, "heating_type": "wood_stove"},
        "components": [
            {"type": Kitchen, "params": {"name": "Il Forno Kitchen", "square_meters": 25, "hob_type": "wood_stove"}},
            {"type": Bathroom, "params": {"name": "Il Forno Bathroom", "square_meters": 8}},
            {"type": Bedroom, "params": {"name": "Stanza Forno", "square_meters": 20, "sleeping_places": 2, "price_history": [(today, Money(250, "EUR"))], "legal_capacity": 2, "actual_capacity": 2, "average_ceiling_height": 2.8, "remarks": "Private Room. Near external wood oven."}},
            {"type": Bedroom, "params": {"name": "Stanza Orto", "square_meters": 18, "sleeping_places": 2, "price_history": [(today, Money(110, "EUR"))], "legal_capacity": 2, "actual_capacity": 2, "average_ceiling_height": 2.8, "remarks": "Shared Room. Overlooks the vegetable garden."}}
        ]
    },
    "Apt. Il Fienile": {
        "params": {"address": brignone_address, "ownership": "owned", "dati_catastali": "Mappale 519, Subalterno 7", "total_square_meters": 55, "heating_type": "wood_stove", "remarks": "Currently uninhabitable, requires full renovation."},
        "components": [
            {"type": Kitchen, "params": {"name": "Il Fienile Kitchen Shell", "square_meters": 15}},
            {"type": Bathroom, "params": {"name": "Il Fienile Bathroom Shell", "square_meters": 5}},
            {"type": Bedroom, "params": {"name": "Il Fienile Bedroom Shell", "square_meters": 35, "sleeping_places": 0, "price_history": [(today, Money(0, "EUR"))], "legal_capacity": 2, "actual_capacity": 0, "average_ceiling_height": 2.7}}
        ]
    },
    "Apt. La Vigna": {
        "params": {"address": brignone_address, "ownership": "owned", "dati_catastali": "Mappale 440 (Primo Piano)", "total_square_meters": 120, "heating_type": "wood_stove", "remarks": "Floor slabs need reconstruction. Uninhabitable."},
        "components": [
            {"type": Kitchen, "params": {"name": "La Vigna Kitchen Shell", "square_meters": 25}},
            {"type": Bathroom, "params": {"name": "La Vigna Bathroom Shell", "square_meters": 10}},
            {"type": Bedroom, "params": {"name": "La Vigna Master Bedroom Shell", "square_meters": 35, "sleeping_places": 0, "price_history": [(today, Money(0, "EUR"))], "legal_capacity": 2, "actual_capacity": 0, "average_ceiling_height": 2.8}},
            {"type": Bedroom, "params": {"name": "La Vigna Second Bedroom Shell", "square_meters": 30, "sleeping_places": 0, "price_history": [(today, Money(0, "EUR"))], "legal_capacity": 2, "actual_capacity": 0, "average_ceiling_height": 2.8}},
            {"type": Bedroom, "params": {"name": "La Vigna Third Bedroom Shell", "square_meters": 20, "sleeping_places": 0, "price_history": [(today, Money(0, "EUR"))], "legal_capacity": 1, "actual_capacity": 0, "average_ceiling_height": 2.8}}
        ]
    },
}

GUESTS_DATA = [
    {"name": "Clara Oswald", "id_code": "UK-CO1986", "nationality": "British", "age": 28, "is_volunteer": True},
    {"name": "Kenji Tanaka", "id_code": "JP-KT1995", "nationality": "Japanese", "age": 30, "is_volunteer": True, "pets": {'dog': 1}},
    {"name": "Fatima Al-Jamil", "id_code": "AE-FA2001", "nationality": "Emirati", "age": 24, "is_volunteer": False},
    {"name": "Liam Murphy", "id_code": "IE-LM1992", "nationality": "Irish", "age": 33, "is_volunteer": True},
    {"name": "Sofia Rossi", "id_code": "IT-SR1998", "nationality": "Italian", "age": 27, "is_volunteer": False, "pets": {'cat': 2}},
    {"name": "David Chen", "id_code": "CA-DC1988", "nationality": "Canadian", "age": 37, "is_volunteer": True},
    {"name": "Anya Sharma", "id_code": "IN-AS2000", "nationality": "Indian", "age": 25, "is_volunteer": True},
    {"name": "Mateo Garcia", "id_code": "ES-MG1999", "nationality": "Spanish", "age": 26, "is_volunteer": False},
]

BOOKINGS_DATA = [
    {"guest_name": "Clara Oswald", "apt_name": "Apt. La Noce", "room_name": "Stanza Fiume", "params": {"room_type": 'shared', "check_in_date": project_start_date, "check_out_date": project_start_date + timedelta(days=90), "payment_amount": Money(100, "EUR"), "payment_type": 'per_period', "payment_frequency": 'monthly', "booking_fee": Money(50, "EUR"), "fee_payment_date": today}},
    {"guest_name": "Kenji Tanaka", "apt_name": "Apt. La Noce", "room_name": "Stanza Fiume", "params": {"room_type": 'shared', "check_in_date": project_start_date + timedelta(days=5), "check_out_date": project_start_date + timedelta(days=65), "payment_amount": Money(100, "EUR"), "payment_type": 'per_period', "payment_frequency": 'monthly', "deposit": Money(100, "EUR")}},
    {"guest_name": "Fatima Al-Jamil", "apt_name": "Apt. La Noce", "room_name": "Stanza Noce", "params": {"room_type": 'private', "check_in_date": project_start_date + timedelta(days=15), "check_out_date": project_start_date + timedelta(days=22), "payment_amount": Money(280, "EUR"), "payment_type": 'total_period', "rent_payments": [(today, Money(280, "EUR"))]}},
    {"guest_name": "Liam Murphy", "apt_name": "Apt. Il Rustico", "room_name": "Stanza Rustico", "params": {"room_type": 'shared', "check_in_date": project_start_date + timedelta(days=20), "check_out_date": date(2026, 1, 30), "payment_amount": Money(90, "EUR"), "payment_type": 'per_period', "payment_frequency": 'monthly'}},
    {"guest_name": "David Chen", "apt_name": "Apt. Il Rustico", "room_name": "Stanza Rustico", "params": {"room_type": 'shared', "check_in_date": date(2025, 12, 1), "check_out_date": date(2026, 3, 15), "payment_amount": Money(90, "EUR"), "payment_type": 'per_period', "payment_frequency": 'monthly'}},
    {"guest_name": "Sofia Rossi", "apt_name": "Apt. Il Forno", "room_name": "Stanza Forno", "params": {"room_type": 'private', "check_in_date": date(2025, 11, 28), "check_out_date": date(2025, 12, 5), "payment_amount": Money(250, "EUR"), "payment_type": 'total_period', "deposit": Money(150, "EUR"), "deposit_payment_date": today}},
    {"guest_name": "Anya Sharma", "apt_name": "Apt. Il Forno", "room_name": "Stanza Orto", "params": {"room_type": 'shared', "check_in_date": date(2026, 1, 10), "check_out_date": date(2026, 3, 10), "payment_amount": Money(110, "EUR"), "payment_type": 'per_period', "payment_frequency": 'monthly'}},
    {"guest_name": "Mateo Garcia", "apt_name": "Apt. Il Forno", "room_name": "Stanza Orto", "params": {"room_type": 'shared', "check_in_date": date(2026, 1, 20), "check_out_date": date(2026, 2, 20), "payment_amount": Money(150, "EUR"), "payment_type": 'total_period', "rent_payments": [(date(2026, 1, 15), Money(150, "EUR"))]}},
]

# ==============================================================================
# OPTIMIZED BUILDER FUNCTION
# ==============================================================================

def populate_register():
    """
    Builds the register by iterating through data structures, which is much
    faster than creating each object individually.
    """
    register = Register(name="Cascina Brignone")
    
    # --- Create Apartments and Rooms ---
    print("--- Initializing Cascina Brignone Property Structure ---")
    for apt_name, apt_data in PROPERTY_DATA.items():
        components = []
        component_map = {}
        for comp_data in apt_data["components"]:
            comp_type = comp_data["type"]
            comp_params = comp_data["params"]
            # Link kitchens and bathrooms to bedrooms
            if comp_type is Bedroom:
                kitchen_name = next((c["params"]["name"] for c in apt_data["components"] if c["type"] is Kitchen), None)
                bathroom_name = next((c["params"]["name"] for c in apt_data["components"] if c["type"] is Bathroom), None)
                if kitchen_name:
                    comp_params["kitchen"] = component_map.get(kitchen_name)
                if bathroom_name:
                    comp_params["bathroom"] = component_map.get(bathroom_name)
            
            component = comp_type(**comp_params)
            components.append(component)
            component_map[component.name] = component
            
        apartment = Apartment(name=apt_name, components=components, **apt_data["params"])
        register.add_apartment(apartment)

    # --- Create Guests ---
    print("\n--- Creating Guests ---")
    guest_map = {g["name"]: Guest(**g) for g in GUESTS_DATA}
    for guest in guest_map.values():
        register.add_guest(guest)

    # --- Create Bookings ---
    print("\n--- Creating Complex Booking Schedule ---")
    # For bulk loading, it's faster to disable the conflict check
    register.enable_conflict_check(False)
    for booking_data in BOOKINGS_DATA:
        guest = guest_map[booking_data["guest_name"]]
        apartment = next(a for a in register.apartments if a.name == booking_data["apt_name"])
        room = next(c for c in apartment.components if c.name == booking_data["room_name"])
        
        register.create_booking(guest=guest, apartment=apartment, room=room, **booking_data["params"])
    
    # Re-enable for any future manual bookings
    register.enable_conflict_check(True)

    return register

# ==============================================================================
# SCRIPT EXECUTION
# ==============================================================================

# Create the register object at the module level so it can be imported
cascina_brignone_register = populate_register()

if __name__ == "__main__":
    print("\nRegister population complete.")
    
    cascina_brignone_register.print_detailed_report()

    print("\n\nTo visualize this new schedule, run the Plotting.py script.")