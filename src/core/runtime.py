from dataclasses import dataclass
from typing import List

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