from datetime import datetime

from src.runtime.runtime_enums import RuntimeStatus

from src.runtime.runtime_transition_models import (
    RuntimeTransitionRecord,
    RuntimeTransitionResult,
)


class RuntimeStateMachine:

    ALLOWED_TRANSITIONS = {

        RuntimeStatus.STARTING: {
            RuntimeStatus.RUNNING,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.RUNNING: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.SAFE_MODE,
            RuntimeStatus.COOLDOWN,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.PAUSED: {
            RuntimeStatus.RUNNING,
            RuntimeStatus.SAFE_MODE,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.SAFE_MODE: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.COOLDOWN: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.EMERGENCY_STOP: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.SHUTDOWN: set(),
    }

    def __init__(
        self,
        runtime_state,
    ):

        self.runtime_state = runtime_state

    @property
    def status(self):

        return self.runtime_state.status

    def can_transition(
        self,
        target_status: RuntimeStatus,
    ) -> bool:

        current_status = (
            self.runtime_state.status
        )

        if (
            current_status
            ==
            RuntimeStatus.SHUTDOWN
        ):
            return False

        allowed_targets = (
            self.ALLOWED_TRANSITIONS
            .get(current_status, set())
        )

        return (
            target_status
            in allowed_targets
        )

    def transition_to(
        self,
        target_status: RuntimeStatus,
        reason: str,
    ) -> RuntimeTransitionResult:

        current_status = (
            self.runtime_state.status
        )

        if (
            current_status
            ==
            RuntimeStatus.EMERGENCY_STOP
            and
            target_status
            ==
            RuntimeStatus.RUNNING
        ):

            raise RuntimeError(
                "Illegal transition: "
                "EMERGENCY_STOP -> RUNNING "
                "requires recovery flow"
            )

        if not self.can_transition(
            target_status
        ):

            raise RuntimeError(
                f"Invalid runtime transition: "
                f"{current_status.value} -> "
                f"{target_status.value}"
            )

        self.runtime_state.status = (
            target_status
        )

        transition_record = (
            RuntimeTransitionRecord(
                previous_state=current_status,
                next_state=target_status,
                reason=reason,
                timestamp=datetime.utcnow(),
            )
        )

        self.runtime_state.transition_history.append(
            transition_record
        )

        return RuntimeTransitionResult(
            success=True,
            previous_state=current_status,
            next_state=target_status,
            reason=reason,
        )

    def is_running(self) -> bool:

        return (
            self.runtime_state.status
            ==
            RuntimeStatus.RUNNING
        )

    def is_paused(self) -> bool:

        return (
            self.runtime_state.status
            ==
            RuntimeStatus.PAUSED
        )

    def is_shutdown(self) -> bool:

        return (
            self.runtime_state.status
            ==
            RuntimeStatus.SHUTDOWN
        )

    def is_emergency_stop(self) -> bool:

        return (
            self.runtime_state.status
            ==
            RuntimeStatus.EMERGENCY_STOP
        )