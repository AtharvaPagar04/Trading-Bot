from src.runtime.governed_runtime import GovernedRuntime
from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)
from src.runtime.event_bus import EventBus

def test_runtime_starts():
    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    assert runtime.state.status == RuntimeStatus.RUNNING


def test_emergency_stop():
    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.emergency_stop(EmergencyReason.MAX_DRAWDOWN)

    assert runtime.state.status == RuntimeStatus.EMERGENCY_STOP
    assert runtime.state.is_trading_enabled is False
    