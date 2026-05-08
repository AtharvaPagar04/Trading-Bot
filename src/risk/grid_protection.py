from enum import Enum


class GridProtectionState(str, Enum):
    NORMAL = "NORMAL"

    DISABLE_BUYS = (
        "DISABLE_BUYS"
    )

    PARTIAL_LIQUIDATION = (
        "PARTIAL_LIQUIDATION"
    )

    EMERGENCY_LIQUIDATION = (
        "EMERGENCY_LIQUIDATION"
    )


def evaluate_grid_protection(
    current_price: float,
    grid_floor: float,
) -> GridProtectionState:
    distance_percent = (
        (
            current_price - grid_floor
        )
        / grid_floor
    ) * 100

    if distance_percent < -4:
        return (
            GridProtectionState
            .EMERGENCY_LIQUIDATION
        )

    if distance_percent <= -2.5:
        return (
            GridProtectionState
            .PARTIAL_LIQUIDATION
        )

    if distance_percent <= -1.5:
        return (
            GridProtectionState
            .DISABLE_BUYS
        )

    return GridProtectionState.NORMAL