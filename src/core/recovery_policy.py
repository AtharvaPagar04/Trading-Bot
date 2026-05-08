from dataclasses import dataclass
from enum import Enum

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_integrity import (
    validate_runtime_integrity,
)

from src.risk.session_risk import (
    SessionRiskState,
)


class RecoveryAction(str, Enum):
    ALLOW_RECOVERY = (
        "ALLOW_RECOVERY"
    )

    REQUIRE_MANUAL_RESUME = (
        "REQUIRE_MANUAL_RESUME"
    )

    FORCE_SAFE_MODE = (
        "FORCE_SAFE_MODE"
    )

    BLOCK_RECOVERY = (
        "BLOCK_RECOVERY"
    )


@dataclass
class RecoveryPolicyResult:
    action: RecoveryAction

    reason: str


def evaluate_recovery_policy(
    runtime: RuntimeState,
) -> RecoveryPolicyResult:

    integrity = (
        validate_runtime_integrity(
            runtime
        )
    )

    if not integrity.valid:
        return RecoveryPolicyResult(
            action=
            RecoveryAction
            .BLOCK_RECOVERY,

            reason=
            "Runtime integrity "
            "validation failed",
        )

    if (
        runtime.risk_state
        .risk_state
        ==
        SessionRiskState
        .EMERGENCY_LIQUIDATION
    ):
        return RecoveryPolicyResult(
            action=
            RecoveryAction
            .FORCE_SAFE_MODE,

            reason=
            "Recovered runtime "
            "was previously "
            "liquidated",
        )

    if (
        not runtime.session
        .entries_enabled
    ):
        return RecoveryPolicyResult(
            action=
            RecoveryAction
            .REQUIRE_MANUAL_RESUME,

            reason=
            "Session entries "
            "disabled before "
            "shutdown",
        )

    return RecoveryPolicyResult(
        action=
        RecoveryAction
        .ALLOW_RECOVERY,

        reason=
        "Runtime recovery "
        "approved",
    )