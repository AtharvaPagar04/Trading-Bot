from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    EmergencyReason,
    RuntimeMode,
    RuntimeStatus,
)

from src.core.events import (
    RuntimeEvent,
    RISK_ALERT,
)

from datetime import datetime


def test_runtime_starts_running():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.RUNNING
    )

    assert (
        runtime.state.is_trading_enabled
        is True
    )


def test_emergency_stop_disables_trading():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    runtime.emergency_stop(
        EmergencyReason.MAX_DRAWDOWN
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.is_trading_enabled
        is False
    )


def test_critical_risk_event_triggers_stop():

    bus = EventBus()

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        bus,
    )

    runtime.start()

    event = RuntimeEvent(
        event_type=
        RISK_ALERT,

        payload={
            "severity":
            "critical"
        },

        timestamp=
        datetime.utcnow(),
    )

    bus.publish(
        event_type=
        RISK_ALERT,

        payload=event,
    )

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.is_trading_enabled
        is False
    )
def test_runtime_can_recover_after_pause():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    runtime.pause()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.PAUSED
    )

    runtime.start()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.RUNNING
    )

    assert (
        runtime.state.is_trading_enabled
        is True
    )