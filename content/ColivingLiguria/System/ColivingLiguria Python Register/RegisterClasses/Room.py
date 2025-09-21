#!/usr/bin/env python3
"""
Room.py

Defines the core components of a rentable property, using a unified inheritance
structure where all specific room types inherit from a common base class.
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
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- Type Definitions ---
# --- EDIT: Added 'none' to allow for kitchens without a hob ---
HobType = Literal['gas', 'induction', 'electric', 'wood', 'none']

# ==============================================================================
# BASE CLASS
# ==============================================================================

class Room:
    """
    A base class for any physical space in the property.
    """
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
        """Generates a summary of the common room features."""
        lines = [
            f"- Size: {self.square_meters} sq. meters",
            f"- Smart Speaker: {'Yes' if self.has_speaker else 'No'}",
            f"- Home Assistant Integrated: {'Yes' if self.is_home_assistant_integrated else 'No'}"
        ]
        if self.remarks:
            lines.append(f"- Remarks: {self.remarks}")
        return "\n".join(lines)

# ==============================================================================
# SUBCLASSES
# ==============================================================================

class Kitchen(Room):
    """Represents a kitchen space, inheriting from Room."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        hob_type: HobType = 'induction',
        has_oven: bool = True,
        has_microwave: bool = False,
        has_fridge: bool = True,
        **kwargs
    ):
        super().__init__(name, square_meters, **kwargs)
        self.hob_type = hob_type
        self.amenities = {
            "Hob": self.hob_type,
            "Oven": has_oven,
            "Microwave": has_microwave,
            "Fridge": has_fridge
        }

    def summary(self) -> str:
        lines = [f"Kitchen: {self.name}"]
        lines.append(super().summary())
        for amenity, value in self.amenities.items():
            display_value = value.capitalize() if isinstance(value, str) else ('Yes' if value else 'No')
            lines.append(f"- {amenity}: {display_value}")
        return "\n".join(lines).replace("\n-", "\n  -")


class Bathroom(Room):
    """Represents a bathroom space, inheriting from Room."""
    def __init__(
        self,
        name: str,
        square_meters: float,
        has_shower: bool = True,
        has_sink: bool = True,
        has_bath: bool = False,
        has_wc: bool = True,
        has_vent: bool = True,
        has_window: bool = False,
        **kwargs
    ):
        super().__init__(name, square_meters, **kwargs)
        self.features = {
            "Shower": has_shower, "Sink": has_sink, "Bath": has_bath,
            "WC": has_wc, "Ventilation": has_vent, "Window": has_window
        }

    def summary(self) -> str:
        lines = [f"Bathroom: {self.name}"]
        lines.append(super().summary())
        for feature, value in self.features.items():
            lines.append(f"- {feature}: {'Yes' if value else 'No'}")
        return "\n".join(lines).replace("\n-", "\n  -")


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

    @property
    def current_price(self) -> Money:
        return self.price_history[-1][1]

    def summary(self) -> str:
        lines = [f"Bedroom: {self.name}"]
        lines.append(super().summary())
        lines.extend([
            f"- Sleeps: {self.sleeping_places} (Actual: {self.actual_capacity}, Legal: {self.legal_capacity})",
            f"- Current Price: {self.current_price}",
            f"- Pets Allowed: {'Yes' if self.allows_pets else 'No'}",
            f"- Uses Kitchen: {self.kitchen.name if self.kitchen else 'None'}",
        ])
        return "\n".join(lines).replace("\n-", "\n  -")


class OtherRoom(Room):
    """Represents a non-bookable, general-purpose room like a living room."""
    def __init__(self, name: str, square_meters: float, has_tv: bool = False, **kwargs):
        super().__init__(name, square_meters, **kwargs)
        self.has_tv = has_tv

    def summary(self) -> str:
        lines = [f"Other Room: {self.name}"]
        lines.append(super().summary())
        lines.append(f"- Has TV: {'Yes' if self.has_tv else 'No'}")
        return "\n".join(lines).replace("\n-", "\n  -")

# --- Example Usage ---
if __name__ == "__main__":
    print("--- DEMONSTRATING NEW INHERITANCE STRUCTURE ---\n")

    # Kitchen now inherits from Room, so it can have remarks and smart features
    main_kitchen = Kitchen(
        name="Main Kitchen",
        square_meters=15,
        hob_type="gas",
        remarks="Newly renovated with marble countertops.",
        is_home_assistant_integrated=True
    )
    print(main_kitchen.summary())
    print("\n" + "="*50 + "\n")

    # Bathroom also inherits from Room
    main_bathroom = Bathroom(
        name="Main Bathroom",
        square_meters=8,
        has_speaker=True
    )
    print(main_bathroom.summary())
    print("\n" + "="*50 + "\n")

    # Bedroom usage remains the same
    master_bedroom = Bedroom(
        name="Master Bedroom",
        square_meters=20,
        sleeping_places=2,
        price_history=[(date.today(), Money(500, "EUR"))],
        legal_capacity=2,
        actual_capacity=2,
        average_ceiling_height=2.7,
        kitchen=main_kitchen,
        bathroom=main_bathroom,
        is_home_assistant_integrated=True
    )
    print(master_bedroom.summary())