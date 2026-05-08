from src.core.recovery_workflow import (
    evaluate_recovery_workflow,
)

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.core.runtime_transition_engine import (
    execute_runtime_transition,
)


def auto_deescalate_runtime(
    runtime: RuntimeState,

    adx_value: float,

    atr_percent: float,

    stable_closes: int,
) -> RuntimeState:

    workflow = (
        evaluate_recovery_workflow(
            runtime=runtime,

            adx_value=
            adx_value,

            atr_percent=
            atr_percent,

            stable_closes=
            stable_closes,
        )
    )

    if not workflow.recovery_allowed:
        return runtime

    current_state = (
        runtime.operating_state
    )

    if (
        current_state
        ==
        RuntimeOperatingState
        .SAFE_MODE
        .value
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .RECOVERY,
        )

        return runtime

    if (
        current_state
        ==
        RuntimeOperatingState
        .RECOVERY
        .value
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .REDUCE_RISK,
        )

        return runtime

    if (
        current_state
        ==
        RuntimeOperatingState
        .REDUCE_RISK
        .value
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .NORMAL,
        )

    return runtime