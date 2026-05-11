from datetime import datetime
from datetime import timedelta
from enum import Enum


class CooldownType(str, Enum):
    MINOR_DRAWDOWN = (
        "MINOR_DRAWDOWN"
    )

    LARGE_DRAWDOWN = (
        "LARGE_DRAWDOWN"
    )

    KILL_SWITCH = "KILL_SWITCH"

    EMERGENCY_LIQUIDATION = (
        "EMERGENCY_LIQUIDATION"
    )


COOLDOWN_DURATIONS = {
    CooldownType.MINOR_DRAWDOWN:
        timedelta(minutes=15),

    CooldownType.LARGE_DRAWDOWN:
        timedelta(hours=1),

    CooldownType.KILL_SWITCH:
        timedelta(hours=2),

    CooldownType.EMERGENCY_LIQUIDATION:
        timedelta(hours=4),
}


def calculate_cooldown_end(
    cooldown_type: CooldownType,
    start_time: datetime,
) -> datetime:
    duration = COOLDOWN_DURATIONS[
        cooldown_type
    ]

    return start_time + duration


def cooldown_active(
    current_time: datetime,
    cooldown_end: datetime,
) -> bool:
    return current_time < cooldown_end