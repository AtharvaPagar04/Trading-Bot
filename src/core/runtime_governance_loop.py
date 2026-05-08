from dataclasses import dataclass

from src.core.monitoring import (
    RuntimeMetrics,
    generate_runtime_metrics,
)

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_auto_escalation import (
    auto_escalate_runtime,
)

from src.core.runtime_deescalation import (
    auto_deescalate_runtime,
)


@dataclass
class GovernanceCycleResult:
    runtime: RuntimeState

    metrics: RuntimeMetrics


def execute_governance_cycle(
    runtime: RuntimeState,

    adx_value: float,

    atr_percent: float,

    stable_closes: int,
) -> GovernanceCycleResult:

    runtime = auto_escalate_runtime(
        runtime
    )

    runtime = auto_deescalate_runtime(
        runtime=runtime,

        adx_value=
        adx_value,

        atr_percent=
        atr_percent,

        stable_closes=
        stable_closes,
    )

    metrics = (
        generate_runtime_metrics(
            runtime
        )
    )

    return GovernanceCycleResult(
        runtime=runtime,

        metrics=metrics,
    )