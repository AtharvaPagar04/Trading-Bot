from src.core.recovery_policy import (
    RecoveryAction,
    evaluate_recovery_policy,
)

from src.core.runtime import (
    RuntimeState,
)


def apply_safe_mode(
    runtime: RuntimeState,
) -> RuntimeState:

    policy = (
        evaluate_recovery_policy(
            runtime
        )
    )

    if (
        policy.action
        ==
        RecoveryAction
        .FORCE_SAFE_MODE
    ):
        runtime.safe_mode = True

        runtime.session.entries_enabled = (
            False
        )

    return runtime