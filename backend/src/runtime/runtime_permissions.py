from src.runtime.runtime_state import (
    RuntimeState,
)

from src.runtime.runtime_enums import (
    RuntimeStatus,
)


BLOCKED_STATUSES = {
    RuntimeStatus.EMERGENCY_STOP,
    RuntimeStatus.SHUTDOWN,
}


def is_execution_allowed(
    runtime_state: RuntimeState,
) -> bool:

    if (
        runtime_state.status
        in BLOCKED_STATUSES
    ):
        return False

    if not runtime_state.is_trading_enabled:
        return False

    return True