from dataclasses import dataclass
from datetime import datetime

from typing import List
from typing import Optional

from src.core.session import (
    TradingSession,
)

from src.core.state import (
    MarketState,
)

from src.events.event import (
    RuntimeEvent,
)

from src.risk.risk_sync import (
    RiskSyncState,
)
from datetime import (
    datetime,
)

@dataclass
class RuntimeState:
    market_state: MarketState
    
    session: TradingSession

    risk_state: RiskSyncState
    safe_mode: bool
    operating_state: str
    active_events: List[RuntimeEvent]
    event_history: List[RuntimeEvent]
    total_trades: int = 0
    winning_trades: int = 0
    losing_trades: int = 0
    latest_price: float = 0.0
    last_execution_price: float = 0.0
    last_execution_time: Optional[datetime] = None
    latest_candle_close: float = 0.0
    latest_candle_timestamp: Optional[datetime] = None
    current_unrealized_pnl: float = 0.0

    current_unrealized_pnl_percent: float = 0.0
    session_started_at: datetime | None = None

    runtime_uptime_seconds: int = 0
    active_session_id: int | None = None

    last_tick_received_at: datetime | None = None

    websocket_connected: bool = False

    reconnect_attempts: int = 0