from datetime import datetime

from src.core.event_bus import EventBus

from src.core.events import (
    RuntimeEvent,
    RISK_ALERT,
)

from src.runtime.governed_runtime import GovernedRuntime

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
)


def test_runtime_emergency_stop_from_risk_event():

    bus = EventBus()

    runtime = GovernedRuntime(
        mode=RuntimeMode.DRY_RUN,
        event_bus=bus,
    )

    event = RuntimeEvent(
        event_type=RISK_ALERT,
        payload={
            "severity": "critical",
        },
        timestamp=datetime.utcnow(),
    )

    bus.publish(event)

    assert runtime.state.status == RuntimeStatus.EMERGENCY_STOP

    assert runtime.state.is_trading_enabled is False
    