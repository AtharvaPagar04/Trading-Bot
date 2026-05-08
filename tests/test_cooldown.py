from datetime import datetime
from datetime import timedelta

from src.risk.cooldown import (
    CooldownType,
    calculate_cooldown_end,
    cooldown_active,
)

start_time = datetime.utcnow()

cooldown_types = [
    CooldownType.MINOR_DRAWDOWN,
    CooldownType.LARGE_DRAWDOWN,
    CooldownType.KILL_SWITCH,
    CooldownType.EMERGENCY_LIQUIDATION,
]

for cooldown_type in cooldown_types:
    cooldown_end = (
        calculate_cooldown_end(
            cooldown_type,
            start_time,
        )
    )

    active = cooldown_active(
        current_time=
        start_time + timedelta(minutes=10),

        cooldown_end=cooldown_end,
    )

    print(
        f"{cooldown_type} | "
        f"Ends: {cooldown_end} | "
        f"Active: {active}"
    )