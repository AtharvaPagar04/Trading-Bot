from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.core.runtime_transition_rules import (
    validate_runtime_transition,
)

valid_transition = (
    validate_runtime_transition(
        current_state=
        RuntimeOperatingState
        .SAFE_MODE,

        target_state=
        RuntimeOperatingState
        .RECOVERY,
    )
)

print("VALID")
print(valid_transition)

invalid_transition = (
    validate_runtime_transition(
        current_state=
        RuntimeOperatingState
        .HALTED,

        target_state=
        RuntimeOperatingState
        .NORMAL,
    )
)

print("\nINVALID")
print(invalid_transition)