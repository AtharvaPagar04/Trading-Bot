from dataclasses import dataclass

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)


@dataclass
class TransitionValidationResult:
    allowed: bool

    reason: str


ALLOWED_TRANSITIONS = {
    RuntimeOperatingState.NORMAL: [
        RuntimeOperatingState.REDUCE_RISK,
        RuntimeOperatingState.SAFE_MODE,
        RuntimeOperatingState.HALTED,
    ],

    RuntimeOperatingState.REDUCE_RISK: [
        RuntimeOperatingState.NORMAL,
        RuntimeOperatingState.SAFE_MODE,
        RuntimeOperatingState.HALTED,
    ],

    RuntimeOperatingState.SAFE_MODE: [
        RuntimeOperatingState.RECOVERY,
        RuntimeOperatingState.HALTED,
    ],

    RuntimeOperatingState.RECOVERY: [
        RuntimeOperatingState.NORMAL,
        RuntimeOperatingState.REDUCE_RISK,
        RuntimeOperatingState.HALTED,
    ],

    RuntimeOperatingState.HALTED: [
        RuntimeOperatingState.RECOVERY,
    ],
}


def validate_runtime_transition(
    current_state: RuntimeOperatingState,

    target_state: RuntimeOperatingState,
) -> TransitionValidationResult:

    allowed_targets = (
        ALLOWED_TRANSITIONS
        .get(current_state, [])
    )

    if target_state in allowed_targets:
        return TransitionValidationResult(
            allowed=True,

            reason=(
                f"Transition allowed: "
                f"{current_state.value}"
                f" -> "
                f"{target_state.value}"
            ),
        )

    return TransitionValidationResult(
        allowed=False,

        reason=(
            f"Invalid transition: "
            f"{current_state.value}"
            f" -> "
            f"{target_state.value}"
        ),
    )