from dataclasses import dataclass
from datetime import datetime

from src.runtime.runtime_enums import RuntimeStatus


@dataclass
class RuntimeTransitionRecord:
    previous_state: RuntimeStatus
    next_state: RuntimeStatus
    reason: str
    timestamp: datetime


@dataclass
class RuntimeTransitionResult:
    success: bool
    previous_state: RuntimeStatus
    next_state: RuntimeStatus
    reason: str