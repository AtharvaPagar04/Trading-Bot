from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)


@dataclass
class RuntimeState:
    mode: RuntimeMode
    status: RuntimeStatus = RuntimeStatus.STARTING

    started_at: datetime = field(default_factory=datetime.utcnow)
    last_heartbeat: datetime = field(default_factory=datetime.utcnow)

    cooldown_until: Optional[datetime] = None

    emergency_reason: Optional[EmergencyReason] = None

    session_pnl: float = 0.0
    session_drawdown: float = 0.0

    active_positions: int = 0
    active_orders: int = 0

    is_trading_enabled: bool = True