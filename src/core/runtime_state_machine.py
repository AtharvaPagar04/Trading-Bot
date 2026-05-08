from dataclasses import dataclass
from enum import Enum

from src.core.runtime import (
    RuntimeState,
)

from src.risk.session_risk import (
    SessionRiskState,
)


class RuntimeOperatingState(
    str,
    Enum,
):
    NORMAL = "NORMAL"

    REDUCE_RISK = (
        "REDUCE_RISK"
    )

    SAFE_MODE = (
        "SAFE_MODE"
    )

    RECOVERY = "RECOVERY"

    HALTED = "HALTED"


@dataclass
class RuntimeStateTransition:
    state: RuntimeOperatingState

    reason: str


def evaluate_runtime_state(
    runtime: RuntimeState,
) -> RuntimeStateTransition:

    if runtime.safe_mode:
        return RuntimeStateTransition(
            state=
            RuntimeOperatingState
            .SAFE_MODE,

            reason=
            "Runtime operating "
            "in safe mode",
        )

    if (
        runtime.risk_state
        .risk_state
        ==
        SessionRiskState
        .EMERGENCY_LIQUIDATION
    ):
        return RuntimeStateTransition(
            state=
            RuntimeOperatingState
            .HALTED,

            reason=
            "Emergency liquidation "
            "state active",
        )

    if (
        runtime.risk_state
        .risk_state
        ==
        SessionRiskState
        .REDUCE_RISK
    ):
        return RuntimeStateTransition(
            state=
            RuntimeOperatingState
            .REDUCE_RISK,

            reason=
            "Runtime operating "
            "under reduced risk",
        )

    if (
        not runtime.session
        .entries_enabled
    ):
        return RuntimeStateTransition(
            state=
            RuntimeOperatingState
            .RECOVERY,

            reason=
            "Runtime recovering "
            "from restricted state",
        )

    return RuntimeStateTransition(
        state=
        RuntimeOperatingState
        .NORMAL,

        reason=
        "Runtime operating "
        "normally",
    )