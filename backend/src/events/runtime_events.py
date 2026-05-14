from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from src.events.base_event import BaseEvent


class RuntimeEventType(Enum):
    START = "runtime_started"
    PAUSE = "runtime_paused"
    STOP = "runtime_stopped"
    RECOVER = "runtime_recovered"
    SHUTDOWN = "runtime_shutdown"
    EMERGENCY_STOP = "runtime_emergency_stop"
    SESSION_START = "session_started"
    SESSION_STOP = "session_stopped"
    TRADING_ENABLED = "trading_enabled"
    TRADING_DISABLED = "trading_disabled"
    SAFE_MODE_TRIGGERED = "safe_mode_triggered"


@dataclass
class RuntimeStartedEvent(BaseEvent):
    pass


@dataclass
class RuntimePausedEvent(BaseEvent):
    reason: str


@dataclass
class RuntimeRecoveredEvent(BaseEvent):
    previous_state: str


@dataclass
class SessionStartedEvent(BaseEvent):
    session_id: int
    started_at: datetime


@dataclass
class SessionStoppedEvent(BaseEvent):
    session_id: int
    stopped_at: datetime
    duration_seconds: int


@dataclass
class TradingEnabledEvent(BaseEvent):
    enabled_by: Optional[str] = None


@dataclass
class TradingDisabledEvent(BaseEvent):
    reason: str


@dataclass
class SafeModeTriggeredEvent(BaseEvent):
    pass