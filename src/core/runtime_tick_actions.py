from dataclasses import dataclass

from src.core.heartbeat import (
    HeartbeatState,
    generate_heartbeat,
)

from src.core.monitoring import (
    RuntimeMetrics,
    generate_runtime_metrics,
)

from src.core.runtime import (
    RuntimeState,
)

from src.persistence.event_store import (
    persist_runtime_events,
)

from src.persistence.runtime_snapshot import (
    persist_runtime_snapshot,
)

from src.persistence.runtime_store import (
    persist_runtime_metrics,
)


@dataclass
class TickActionResult:
    heartbeat: HeartbeatState

    metrics: RuntimeMetrics


def execute_tick_actions(
    runtime: RuntimeState,
) -> TickActionResult:

    heartbeat = generate_heartbeat(
        runtime
    )

    metrics = (
        generate_runtime_metrics(
            runtime
        )
    )

    persist_runtime_metrics(
        metrics
    )

    persist_runtime_events(
        runtime.event_history
    )

    persist_runtime_snapshot(
        runtime
    )

    return TickActionResult(
        heartbeat=heartbeat,

        metrics=metrics,
    )