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

from src.strategy.strategy_state import (
    StrategyState,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)

from src.risk.drawdown_tracker import (
    DrawdownState,
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
        runtime=runtime,

        strategy_state=
        StrategyState(),

        portfolio=
        PaperPortfolio(),

        drawdown_state=
        DrawdownState(
            peak_equity=
            runtime.session.current_capital,

            current_drawdown_percent=0.0,
        ),
    )

    return TickActionResult(
        heartbeat=heartbeat,

        metrics=metrics,
    )