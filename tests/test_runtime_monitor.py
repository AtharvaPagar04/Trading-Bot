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
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    monitor = RuntimeMonitor(
        runtime
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