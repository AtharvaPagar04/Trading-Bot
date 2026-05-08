from dataclasses import dataclass


@dataclass
class DynamicPositionSizing:

    base_quantity: float

    confidence_multiplier: float

    adjusted_quantity: float