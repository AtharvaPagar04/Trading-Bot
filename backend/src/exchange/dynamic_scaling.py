from src.exchange.dynamic_scaling_models import (
    DynamicPositionSizing,
)


def apply_confidence_scaling(
    quantity: float,

    confidence_multiplier: float,
) -> DynamicPositionSizing:

    adjusted_quantity = (
        quantity
        * confidence_multiplier
    )

    return DynamicPositionSizing(
        base_quantity=
        quantity,

        confidence_multiplier=
        confidence_multiplier,

        adjusted_quantity=
        adjusted_quantity,
    )