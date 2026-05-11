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