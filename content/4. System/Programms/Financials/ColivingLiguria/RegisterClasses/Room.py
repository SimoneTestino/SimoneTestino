#!/usr/bin/env python3
"""
Room.py

Defines the core components of a rentable property, using inheritance
for different room types.
"""

from __future__ import annotations
import sys
import os
from datetime import date
from typing import List, Tuple, Optional, Literal
from moneyed import Money
import warnings

# --- Path Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
register_classes_dir = os.path.dirname(current_dir)
coliving_dir = os.path.dirname(register_classes_dir)
project_root = os.path.dirname(coliving_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Imports ---
HobType = Literal['gas', 'induction', 'electric']

class Kitchen:
    """Represents a kitchen space in a property."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        hob_type: HobType = 'induction',
        has_oven: bool = True,
        has_microwave: bool = False,
        has_fridge: bool = True
    ):
        self.name = name
        self.square_meters = square_meters
        self.hob_type = hob_type
        self.amenities = { "Hob": self.hob_type, "Oven": has_oven, "Microwave": has_microwave, "Fridge": has_fridge }

    def summary(self) -> str:
        lines = [f"Kitchen: {self.name}", f"- Size: {self.square_meters} sq. meters"]
        for amenity, value in self.amenities.items():
            lines.append(f"- {amenity}: {value.capitalize() if isinstance(value, str) else ('Yes' if value else 'No')}")
        return "\n".join(lines)

class Bathroom:
    """Represents a bathroom space in a property."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        has_shower: bool = True,
        has_sink: bool = True,
        has_bath: bool = False,
        has_wc: bool = True,
        has_vent: bool = True,
        has_window: bool = False
    ):
        self.name = name
        self.square_meters = square_meters
        self.features = { "Shower": has_shower, "Sink": has_sink, "Bath": has_bath, "WC": has_wc, "Ventilation": has_vent, "Window": has_window }

    def summary(self) -> str:
        lines = [f"Bathroom: {self.name}", f"- Size: {self.square_meters} sq. meters"]
        for feature, value in self.features.items():
            lines.append(f"- {feature}: {'Yes' if value else 'No'}")
        return "\n".join(lines)

class Room:
    """A base class for any room in the property."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        remarks: Optional[str] = None,
        has_speaker: bool = False,
        is_home_assistant_integrated: bool = False
    ):
        self.name = name
        self.square_meters = square_meters
        self.remarks = remarks
        self.has_speaker = has_speaker
        self.is_home_assistant_integrated = is_home_assistant_integrated

    def summary(self) -> str:
        lines = [
            f"- Size: {self.square_meters} sq. meters",
            f"- Smart Speaker: {'Yes' if self.has_speaker else 'No'}",
            f"- Home Assistant Integrated: {'Yes' if self.is_home_assistant_integrated else 'No'}"
        ]
        if self.remarks:
            lines.append(f"- Remarks: {self.remarks}")
        return "\n".join(lines)

class Bedroom(Room):
    """Represents a bookable bedroom, inheriting from the base Room class."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        sleeping_places: int,
        price_history: List[Tuple[date, Money]],
        legal_capacity: int,
        actual_capacity: int,
        average_ceiling_height: float,
        min_ceiling_height: Optional[float] = None,
        kitchen: Optional[Kitchen] = None,
        bathroom: Optional[Bathroom] = None,
        has_terrace: bool = False,
        allows_pets: bool = False,
        **kwargs
    ):
        super().__init__(name, square_meters, **kwargs)
        if not price_history:
            raise ValueError("A Bedroom must have at least one price in its price_history.")
        
        self.sleeping_places = sleeping_places
        self.price_history = sorted(price_history, key=lambda x: x[0])
        self.legal_capacity = legal_capacity
        self.actual_capacity = actual_capacity
        self.average_ceiling_height = average_ceiling_height
        self.min_ceiling_height = min_ceiling_height or average_ceiling_height
        self.kitchen = kitchen
        self.bathroom = bathroom
        self.has_terrace = has_terrace
        self.allows_pets = allows_pets
        
        if not self.kitchen: warnings.warn(f"Bedroom '{self.name}' has no Kitchen assigned.", UserWarning)
        if not self.bathroom: warnings.warn(f"Bedroom '{self.name}' has no Bathroom assigned.", UserWarning)
        if self.legal_capacity > self.actual_capacity:
            warnings.warn(f"Bedroom '{self.name}': Legal capacity ({self.legal_capacity}) cannot be greater than actual capacity ({self.actual_capacity}).", UserWarning)
        
        self._check_italian_regulations()

    def _check_italian_regulations(self):
        if self.min_ceiling_height < 2.70:
            warnings.warn(f"Bedroom '{self.name}': Minimum ceiling height ({self.min_ceiling_height}m) is below the standard 2.70m.", UserWarning)
        
        required_sqm = 0
        if self.legal_capacity == 1: required_sqm = 9
        elif self.legal_capacity == 2: required_sqm = 14
        
        if required_sqm > 0 and self.square_meters < required_sqm:
            warnings.warn(f"Bedroom '{self.name}': Size ({self.square_meters}sqm) may be insufficient for its legal capacity of {self.legal_capacity} person(s). Standard is {required_sqm}sqm.", UserWarning)

    @property
    def current_price(self) -> Money:
        return self.price_history[-1][1]

    def summary(self) -> str:
        lines = [f"Bedroom: {self.name}"]
        lines.append(super().summary())
        lines.extend([
            f"- Sleeps: {self.sleeping_places} (Actual: {self.actual_capacity}, Legal: {self.legal_capacity})",
            f"- Ceiling Height: {self.average_ceiling_height}m avg, {self.min_ceiling_height}m min",
            f"- Current Price: {self.current_price}",
            f"- Has Terrace: {'Yes' if self.has_terrace else 'No'}",
            f"- Pets Allowed: {'Yes' if self.allows_pets else 'No'}",
            f"- Uses Kitchen: {self.kitchen.name if self.kitchen else 'None'}",
            f"- Uses Bathroom: {self.bathroom.name if self.bathroom else 'None'}"
        ])
        return "\n".join(lines).replace("\n-", "\n  -")

class OtherRoom(Room):
    """Represents a non-bookable, general-purpose room."""
    def __init__(self, name: str, square_meters: float, has_tv: bool = False, **kwargs):
        super().__init__(name, square_meters, **kwargs)
        self.has_tv = has_tv
    
    def summary(self) -> str:
        lines = [f"Other Room: {self.name}"]
        lines.append(super().summary())
        lines.append(f"- Has TV: {'Yes' if self.has_tv else 'No'}")
        return "\n".join(lines).replace("\n-", "\n  -")