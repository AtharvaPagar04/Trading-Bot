from dataclasses import dataclass
from datetime import datetime

from src.events.base_event import BaseEvent

@dataclass
class RuntimeEvent(BaseEvent):
    payload: dict


MARKET_TICK = (
    "MARKET_TICK"
)

NEW_CANDLE = (
    "NEW_CANDLE"
)

SIGNAL_GENERATED = (
    "SIGNAL_GENERATED"
)

ORDER_EXECUTED = (
    "ORDER_EXECUTED"
)

POSITION_UPDATED = (
    "POSITION_UPDATED"
)

RISK_ALERT = (
    "RISK_ALERT"
)

REBALANCE_TRIGGERED = (
    "REBALANCE_TRIGGERED"
)

SYSTEM_RECALIBRATION = (
    "SYSTEM_RECALIBRATION"
)