from src.core.runtime_builder import (
    build_runtime_state,
)
from datetime import datetime
from datetime import timedelta

from src.runtime.event_bus import EventBus

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_monitor import (
    RuntimeMonitor,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)


def test_monitor_detects_expired_heartbeat():

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

    monitor = RuntimeMonitor(
        runtime=runtime,
        exchange=MockExchange(),
    )

    runtime.state.last_heartbeat = (
        datetime.utcnow()
        -
        timedelta(seconds=31)
    )

    monitor.tick()

    assert (
        runtime.state.status
        ==
        RuntimeStatus.EMERGENCY_STOP
    )

    assert (
        runtime.state.emergency_reason
        ==
        EmergencyReason
        .HEARTBEAT_FAILURE
    )

class MockExchange:

    def portfolio_reconciliation_valid(
        self,
        latest_price,
    ):
        return True