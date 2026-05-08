from dataclasses import dataclass


@dataclass
class GridAnchorState:
    anchor_price: float
    reanchor_allowed: bool


def create_initial_anchor(
    current_price: float,
) -> float:
    return current_price


def validate_reanchor_conditions(
    outside_range_minutes: int,
    adx_value: float,
    atr_percent: float,
    emergency_active: bool,
) -> bool:
    return all(
        [
            outside_range_minutes > 30,
            adx_value < 25,
            atr_percent < 3,
            not emergency_active,
        ]
    )


def build_anchor_state(
    current_price: float,
    outside_range_minutes: int,
    adx_value: float,
    atr_percent: float,
    emergency_active: bool,
) -> GridAnchorState:
    return GridAnchorState(
        anchor_price=
        current_price,

        reanchor_allowed=
        validate_reanchor_conditions(
            outside_range_minutes=
            outside_range_minutes,

            adx_value=
            adx_value,

            atr_percent=
            atr_percent,

            emergency_active=
            emergency_active,
        ),
    )