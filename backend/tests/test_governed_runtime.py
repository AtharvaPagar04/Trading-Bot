from src.core.runtime_builder import (
    build_runtime_state,
)
from src.runtime.governed_runtime import GovernedRuntime
from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)
from src.runtime.event_bus import EventBus
from datetime import timedelta
from datetime import datetime

from datetime import timedelta
from datetime import datetime

def test_runtime_starts():
    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    assert runtime.state.status == RuntimeStatus.RUNNING


def test_emergency_stop():
    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.emergency_stop(EmergencyReason.MAX_DRAWDOWN)

    assert runtime.state.status == RuntimeStatus.EMERGENCY_STOP
    assert runtime.state.is_trading_enabled is False
def test_heartbeat_failure_triggers_emergency_stop():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.state.last_heartbeat = (
        datetime.utcnow()
        -
        timedelta(seconds=31)
    )

    runtime.validate_heartbeat()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.emergency_reason
        ==
        EmergencyReason.HEARTBEAT_FAILURE
    )

    assert (
        runtime.execution_allowed()
        is False
    )

def test_stale_market_data_triggers_emergency_stop():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)
    runtime.start()
    runtime.state.last_tick_received_at = (
        datetime.utcnow()
        -
        timedelta(seconds=25)
    )

    runtime.validate_market_data()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.emergency_reason
        ==
        EmergencyReason.TRANSPORT_FAILURE
    )

    assert (
        runtime.execution_allowed()
        is False
    )
def test_runtime_recovery():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.emergency_stop(
        EmergencyReason
        .HEARTBEAT_FAILURE
    )

    runtime.recover()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.PAUSED
    )

    assert (
        runtime.state.emergency_reason
        is None
    )

    assert (
        runtime.execution_allowed()
        is True
    )
def test_runtime_cooldown_activation():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    runtime.activate_cooldown(
        seconds=30
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.COOLDOWN
    )

    assert (
        runtime.state.cooldown_until
        is not None
    )

    assert (
        runtime.execution_allowed()
        is False
    )

def test_cooldown_expiry_transitions_to_paused():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
    EventBus(),
)

    runtime.start()

    runtime.activate_cooldown(
        seconds=0
    )

    runtime.validate_cooldown()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.PAUSED
    )

    assert (
        runtime.state.cooldown_until
        is None
    )

    assert (
        runtime.execution_allowed()
        is True
    )