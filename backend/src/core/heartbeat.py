from dataclasses import dataclass
from datetime import datetime

from src.core.runtime import (
    RuntimeState,
)


@dataclass
class HeartbeatState:
    timestamp: datetime

    active_event_count: int

    archived_event_count: int

    runtime_healthy: bool


def generate_heartbeat(
    runtime: RuntimeState,
) -> HeartbeatState:
    runtime_healthy = all(
        [
            runtime.market_state is not None,
            runtime.session is not None,
            runtime.risk_state is not None,
        ]
    )

    return HeartbeatState(
        timestamp=datetime.utcnow(),

        active_event_count=len(
            runtime.active_events
        ),

        archived_event_count=len(
            runtime.event_history
        ),

        runtime_healthy=
        runtime_healthy,
    )