from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.core.runtime_transition_rules import (
    validate_runtime_transition,
)

from src.events.event import (
    EventType,
)

from src.events.event_factory import (
    create_event,
)


@dataclass
class RuntimeTransitionResult:
    success: bool

    reason: str


def execute_runtime_transition(
    runtime: RuntimeState,

    target_state: RuntimeOperatingState,
) -> RuntimeTransitionResult:

    current_state = (
        RuntimeOperatingState(
            runtime.operating_state
        )
    )

    validation = (
        validate_runtime_transition(
            current_state=
            current_state,

            target_state=
            target_state,
        )
    )

    if not validation.allowed:
        return RuntimeTransitionResult(
            success=False,

            reason=validation.reason,
        )
# Compatibility mutation layer.
# operating_state is being phased out as
# authoritative runtime state in favor of
# computed governance projection access.
    runtime.operating_state = (
        target_state.value
    )

    runtime.active_events.append(
        create_event(
            EventType.RUNTIME_STATE_CHANGED,

            (
                f"Runtime transitioned "
                f"from "
                f"{current_state.value}"
                f" to "
                f"{target_state.value}"
            ),
        )
    )

    return RuntimeTransitionResult(
        success=True,

        reason=validation.reason,
    )