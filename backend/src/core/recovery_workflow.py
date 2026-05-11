from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.risk.recovery import (
    validate_reentry_conditions,
)


@dataclass
class RecoveryWorkflowResult:
    recovery_allowed: bool

    reason: str


def evaluate_recovery_workflow(
    runtime: RuntimeState,

    adx_value: float,

    atr_percent: float,

    stable_closes: int,
) -> RecoveryWorkflowResult:

    if runtime.safe_mode:
        return RecoveryWorkflowResult(
            recovery_allowed=False,

            reason=
            "Runtime still "
            "in safe mode",
        )

    reentry = (
        validate_reentry_conditions(
            adx_value=adx_value,

            atr_percent=
            atr_percent,

            stable_candle_closes=
            stable_closes,
        )
    )

    if not reentry.reentry_allowed:
        return RecoveryWorkflowResult(
            recovery_allowed=False,

            reason=
            "Market recovery "
            "conditions not met",
        )

    return RecoveryWorkflowResult(
        recovery_allowed=True,

        reason=
        "Recovery workflow "
        "approved",
    )