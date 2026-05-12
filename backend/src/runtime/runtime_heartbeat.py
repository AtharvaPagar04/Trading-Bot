from datetime import datetime, timedelta

from src.runtime.runtime_state import (
    RuntimeState,
)


HEARTBEAT_TIMEOUT_SECONDS = 30
STALE_FEED_TIMEOUT_SECONDS = 20

def heartbeat_expired(
    runtime_state: RuntimeState,
) -> bool:

    now = datetime.utcnow()

    timeout_threshold = (
        runtime_state.last_heartbeat
        +
        timedelta(
            seconds=
            HEARTBEAT_TIMEOUT_SECONDS
        )
    )

    return now > timeout_threshold

def market_feed_stale(
    runtime_state: RuntimeState,
) -> bool:

    if (
        runtime_state.last_tick_received_at
        is None
    ):
        return True

    now = datetime.utcnow()

    timeout_threshold = (
        runtime_state.last_tick_received_at
        +
        timedelta(
            seconds=
            STALE_FEED_TIMEOUT_SECONDS
        )
    )

    return now > timeout_threshold
def synchronize_transport_state(
    runtime_state: RuntimeState,
) -> None:

    runtime_state.websocket_connected = (
        not market_feed_stale(
            runtime_state
        )
    )