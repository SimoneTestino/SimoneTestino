#!/usr/bin/env python3
"""
Apartment.py

Defines the Apartment class, which acts as a container for various rooms
and facilities, and tracks detailed property information.
"""
from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Optional, Literal, Dict
import warnings

# --- Path Setup ---
# Ensures the script can find other modules in the same directory
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- Imports ---
# Corrected to use direct imports for consistency within the package
from RegisterClasses.Room import Room, Bedroom, OtherRoom, Kitchen, Bathroom
from moneyed import Money

# --- Type Definitions ---
HeatingType = Literal['none', 'gas_radiators', 'electric_radiators', 'underfloor', 'heat_pump', 'pellet_stove', 'wood_stove', 'petrol_stove', 'centralized']
EnergyClass = Literal['A4', 'A3', 'A2', 'A1', 'B', 'C', 'D', 'E', 'F', 'G']
DoorType = Literal['normal', 'reinforced', 'digital_lock']
OwnershipType = Literal['owned', 'managed']

class Apartment:
    """
    Represents a single apartment unit, composed of various rooms and facilities.
    """
    def __init__(
        self,
        name: str,
        components: List[Room],
        address: str,
        dati_catastali: str,
        ownership: OwnershipType,
        total_square_meters: Optional[float] = None,
        heating_type: HeatingType = 'gas_radiators',
        energy_class: Optional[EnergyClass] = None,
        insulation_comment: Optional[str] = None,
        has_double_glazing: bool = True,
        door_type: DoorType = 'normal',
        garden_details: Optional[Dict] = None,
        wifi_details: Optional[Dict] = None,
        home_assistant_coverage_pct: Optional[float] = None,
        stairs_connection: Optional[Dict] = None,
        # --- FIX: Added the missing 'remarks' parameter ---
        remarks: Optional[str] = None
    ):
        self.name = name
        self.components = components
        self.address = address
        self.dati_catastali = dati_catastali
        self.ownership = ownership
        self._total_square_meters = total_square_meters
        self.heating_type = heating_type
        self.energy_class = energy_class
        self.insulation_comment = insulation_comment
        self.has_double_glazing = has_double_glazing
        self.door_type = door_type
        self.garden_details = garden_details or {}
        self.wifi_details = wifi_details or {}
        self.home_assistant_coverage_pct = home_assistant_coverage_pct
        self.stairs_connection = stairs_connection or {}
        self.remarks = remarks # Assign the new property

        self._validate_components()
        self.check_sqm_discrepancy()

    def _validate_components(self):
        if not any(isinstance(c, Bedroom) for c in self.components):
            raise ValueError(f"Apartment '{self.name}' must have at least one Bedroom.")
        if not any(isinstance(c, Kitchen) for c in self.components):
            raise ValueError(f"Apartment '{self.name}' must have at least one Kitchen.")
        if not any(isinstance(c, Bathroom) for c in self.components):
            raise ValueError(f"Apartment '{self.name}' must have at least one Bathroom.")

    def get_bedrooms(self) -> List[Bedroom]:
        """Returns a list of all Bedroom components in the apartment."""
        return [c for c in self.components if isinstance(c, Bedroom)]

    def get_component_by_name(self, name: str) -> Optional[Room]:
        """Finds and returns a component by its exact name."""
        for component in self.components:
            if component.name == name:
                return component
        return None

    @property
    def components_square_meters(self) -> float:
        return sum(c.square_meters for c in self.components)

    @property
    def total_square_meters(self) -> float:
        return self._total_square_meters or self.components_square_meters

    @property
    def unregistered_sqm_pct(self) -> float:
        if self._total_square_meters is None or self._total_square_meters == 0:
            return 0.0
        unregistered = self._total_square_meters - self.components_square_meters
        return (unregistered / self._total_square_meters) * 100

    def check_sqm_discrepancy(self):
        if self._total_square_meters is not None and self._total_square_meters < self.components_square_meters:
            warnings.warn(f"Apartment '{self.name}': Provided total square meters is LESS than the sum of its components.", UserWarning)

    @property
    def home_assistant_coverage(self) -> float:
        if self.home_assistant_coverage_pct is not None:
            return self.home_assistant_coverage_pct
        if not self.components:
            return 0.0
        integrated_rooms = sum(1 for c in self.components if getattr(c, 'is_home_assistant_integrated', False))
        return (integrated_rooms / len(self.components)) * 100

    def summary(self) -> str:
        component_names = ', '.join([c.name for c in self.components])
        lines = [
            f"Apartment Summary: {self.name}",
            f"  Address: {self.address}",
            f"  Cadastral Data: {self.dati_catastali}",
            f"  Ownership: {self.ownership.capitalize()}",
            f"  Total Area: {self.total_square_meters} sqm",
            f"  Heating: {self.heating_type.replace('_', ' ').capitalize()}",
            f"  Energy Class: {self.energy_class or 'N/A'}",
            f"  Components ({len(self.components)}): {component_names}"
        ]
        # --- FIX: Display remarks in the summary if they exist ---
        if self.remarks:
            lines.append(f"  Remarks: {self.remarks}")
        return "\n".join(lines)

# --- Example Usage ---
if __name__ == "__main__":
    kitchen = Kitchen(name="Main Kitchen", square_meters=15, hob_type="gas")
    bathroom = Bathroom(name="Main Bathroom", square_meters=8)
    bedroom1 = Bedroom(
        name="Master Bedroom", square_meters=20, sleeping_places=2,
        price_history=[(date.today(), Money(500, "EUR"))],
        legal_capacity=2, actual_capacity=2, average_ceiling_height=2.7,
        kitchen=kitchen, bathroom=bathroom, is_home_assistant_integrated=True
    )
    living_room = OtherRoom(name="Living Room", square_meters=30, has_tv=True)

    my_apartment = Apartment(
        name="Apt. 1 - 'Il Sole'",
        components=[kitchen, bathroom, bedroom1, living_room],
        address="Via Roma 1, 17100 Savona SV",
        dati_catastali="Foglio 12, Particella 345, Sub 6",
        ownership="owned",
        total_square_meters=100,
        energy_class="C",
        remarks="Ready for guests."
    )

    print(my_apartment.summary())