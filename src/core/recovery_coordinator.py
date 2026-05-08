from dataclasses import dataclass
from datetime import datetime

from src.core.recovery_workflow import (
    evaluate_recovery_workflow,
)

from src.core.runtime import (
    RuntimeState,
)

from src.risk.cooldown import (
    cooldown_active,
)


@dataclass
class CoordinatedRecoveryResult:
    recovery_allowed: bool

    reason: str


def evaluate_coordinated_recovery(
    runtime: RuntimeState,

    cooldown_end: datetime,

    current_time: datetime,

    adx_value: float,

    atr_percent: float,

    stable_closes: int,
) -> CoordinatedRecoveryResult:

    if cooldown_active(
        current_time=
        current_time,

        cooldown_end=
        cooldown_end,
    ):
        return CoordinatedRecoveryResult(
            recovery_allowed=False,

            reason=
            "Cooldown still active",
        )

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
        return CoordinatedRecoveryResult(
            recovery_allowed=False,

            reason=workflow.reason,
        )

    return CoordinatedRecoveryResult(
        recovery_allowed=True,

        reason=
        "Coordinated recovery "
        "approved",
    )