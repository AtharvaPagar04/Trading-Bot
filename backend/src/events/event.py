from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(str, Enum):
    SESSION_STARTED = (
        "SESSION_STARTED"
    )

    TRADE_EXECUTED = (
        "TRADE_EXECUTED"
    )

    RISK_ESCALATED = (
        "RISK_ESCALATED"
    )

    COOLDOWN_STARTED = (
        "COOLDOWN_STARTED"
    )

    REENTRY_ALLOWED = (
        "REENTRY_ALLOWED"
    )

    GRID_REANCHORED = (
        "GRID_REANCHORED"
    )

    EMERGENCY_LIQUIDATION = (
        "EMERGENCY_LIQUIDATION"
    )
    RUNTIME_STATE_CHANGED = (
        "RUNTIME_STATE_CHANGED"
    )


@dataclass
class RuntimeEvent:
    event_type: EventType

    timestamp: datetime

    message: str