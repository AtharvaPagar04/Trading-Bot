from src.core.runtime_builder import (
    build_runtime_state,
)
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
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=bus,
)

    event = RuntimeEvent(
        event_type=RISK_ALERT,
        payload={
            "severity": "critical",
        },
        emitted_at=datetime.utcnow(),
    )

    bus.publish(event)

    assert runtime.state.status == RuntimeStatus.EMERGENCY_STOP

    assert runtime.state.is_trading_enabled is False
    