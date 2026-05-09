from datetime import datetime

from src.runtime.runtime_state import RuntimeState

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)

from src.runtime.runtime_permissions import (
    is_execution_allowed,
)

from src.runtime.event_bus import EventBus

from src.runtime.runtime_heartbeat import (
    heartbeat_expired,
)
from datetime import timedelta
from src.runtime.market_data_health import (
    MarketDataHealth,
)

from src.core.events import (
    RuntimeEvent,
    RISK_ALERT,
    SYSTEM_RECALIBRATION,
)


class GovernedRuntime:

    ALLOWED_TRANSITIONS = {
        RuntimeStatus.STARTING: {
            RuntimeStatus.RUNNING,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.RUNNING: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.COOLDOWN,
            RuntimeStatus.EMERGENCY_STOP,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.PAUSED: {
            RuntimeStatus.RUNNING,
            RuntimeStatus.SHUTDOWN,
        },

        RuntimeStatus.COOLDOWN: {
            RuntimeStatus.PAUSED,
            RuntimeStatus.RUNNING,
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
        mode: RuntimeMode,
        event_bus: EventBus,
    ):

        self.state = RuntimeState(
            mode=mode
        )

        self.event_bus = event_bus

        self.market_data_health = (
            MarketDataHealth(
                last_update=
                datetime.utcnow()
            )
        )

        self._register_handlers()

    def _register_handlers(self):

        self.event_bus.subscribe(
            RISK_ALERT,
            self.handle_risk_alert,
        )

        self.event_bus.subscribe(
            SYSTEM_RECALIBRATION,
            self.handle_recalibration,
        )

    def start(self):

        self.transition_to(
            RuntimeStatus.RUNNING
        )

        self.state.last_heartbeat = (
            datetime.utcnow()
        )

    def pause(self):

        self.transition_to(
            RuntimeStatus.PAUSED
        )

    def emergency_stop(
        self,
        reason: EmergencyReason,
    ):

        self.transition_to(
            RuntimeStatus
            .EMERGENCY_STOP
        )

        self.state.emergency_reason = (
            reason
        )

        self.state.is_trading_enabled = (
            False
        )
        
    def recover(self):

        self.transition_to(
            RuntimeStatus.PAUSED
        )

        self.state.emergency_reason = (
            None
        )

        self.state.is_trading_enabled = (
            True
        )
        
    def activate_cooldown(
        self,
        seconds: int = 30,
    ):

        self.transition_to(
            RuntimeStatus.COOLDOWN
        )

        self.state.cooldown_until = (
            datetime.utcnow()
            +
            timedelta(
                seconds=seconds
            )
        )

        self.state.is_trading_enabled = (
            False
        )
    
    def validate_cooldown(self):

        if (
            self.state.status
            !=
            RuntimeStatus.COOLDOWN
        ):
            return

        if (
            self.state.cooldown_until
            is None
        ):
            return

        if (
            datetime.utcnow()
            >=
            self.state.cooldown_until
        ):

            self.transition_to(
                RuntimeStatus.PAUSED
            )

            self.state.is_trading_enabled = (
                True
            )

            self.state.cooldown_until = (
                None
            )

    def heartbeat(self):

        self.state.last_heartbeat = (
            datetime.utcnow()
        )

    def market_data_heartbeat(self):

        self.market_data_health.update()

    def validate_heartbeat(self):

        if heartbeat_expired(
            self.state
        ):

            self.emergency_stop(
                EmergencyReason
                .HEARTBEAT_FAILURE
            )

    def validate_market_data(self):

        if (
            self.market_data_health
            .is_stale()
        ):

            self.emergency_stop(
                EmergencyReason
                .HEARTBEAT_FAILURE
            )

    def execution_allowed(
        self,
    ) -> bool:

        return is_execution_allowed(
            self.state
        )

    def shutdown(self):

        self.transition_to(
            RuntimeStatus.SHUTDOWN
        )

    def handle_risk_alert(
        self,
        event: RuntimeEvent,
    ):

        severity = (
            event.payload
            .get("severity")
        )

        if severity == "critical":

            self.emergency_stop(
                EmergencyReason
                .MAX_DRAWDOWN,
            )

    def handle_recalibration(
        self,
        event: RuntimeEvent,
    ):

        self.pause()

    def transition_to(
        self,
        target_status: RuntimeStatus,
    ):

        current_status = (
            self.state.status
        )

        allowed_targets = (
            self.ALLOWED_TRANSITIONS
            .get(
                current_status,
                set(),
            )
        )

        if (
            target_status
            not in allowed_targets
        ):

            raise RuntimeError(
                f"Invalid runtime "
                f"transition: "
                f"{current_status}"
                f" -> "
                f"{target_status}"
            )

        self.state.status = (
            target_status
        )