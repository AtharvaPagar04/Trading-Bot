from datetime import datetime, timedelta

from src.runtime.runtime_state import (
    RuntimeState,
)


HEARTBEAT_TIMEOUT_SECONDS = 30


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