from dataclasses import dataclass
from datetime import datetime

from typing import List
from typing import Optional
from dataclasses import field

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
from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)
from src.runtime.runtime_transition_models import (
    RuntimeTransitionRecord,
)
@dataclass
class RuntimeState:
    market_state: MarketState
    
    session: TradingSession


    risk_state: RiskSyncState
    safe_mode: bool
    
    active_events: List[RuntimeEvent]
    event_history: List[RuntimeEvent]
    transition_history: List[
        RuntimeTransitionRecord
    ] = field(
        default_factory=list
    )
    
    total_trades: int = 0
    winning_trades: int = 0
    losing_trades: int = 0
    latest_price: float = 0.0
    operating_state: str | None = None
# Deprecated synchronized projection state.
# Use get_operating_state(runtime) for computed access.
# Remaining mutable usage exists only for staged
# recovery/deescalation workflow compatibility.
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

    mode: RuntimeMode = RuntimeMode.DRY_RUN

    status: RuntimeStatus = (
        RuntimeStatus.STARTING
    )

    started_at: datetime = field(
        default_factory=datetime.utcnow
    )

    last_heartbeat: datetime = field(
        default_factory=datetime.utcnow
    )

    cooldown_until: Optional[datetime] = None

    emergency_reason: Optional[
        EmergencyReason
    ] = None

    session_pnl: float = 0.0

    session_drawdown: float = 0.0

    active_positions: int = 0

    active_orders: int = 0

    is_trading_enabled: bool = True