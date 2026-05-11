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
    total_trades: int = 0

    winning_trades: int = 0
    losing_trades: int = 0
    latest_price: float = 0.0

    last_execution_price: float = 0.0
    last_execution_time: Optional[datetime] = None
    latest_candle_close: float = 0.0

    latest_candle_timestamp: Optional[datetime] = None

    is_trading_enabled: bool = True