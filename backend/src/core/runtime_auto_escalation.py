from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.core.runtime_transition_engine import (
    execute_runtime_transition,
)

from src.risk.session_risk import (
    SessionRiskState,
)


def auto_escalate_runtime(
    runtime: RuntimeState,
) -> RuntimeState:

    if runtime.safe_mode:
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .SAFE_MODE,
        )

        return runtime

    if (
        runtime.risk_state
        .risk_state
        ==
        SessionRiskState
        .EMERGENCY_LIQUIDATION
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .HALTED,
        )

        return runtime

    if (
        runtime.risk_state
        .risk_state
        ==
        SessionRiskState
        .REDUCE_RISK
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .REDUCE_RISK,
        )

        return runtime

    if (
        not runtime.session
        .entries_enabled
    ):
        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .RECOVERY,
        )

    return runtime