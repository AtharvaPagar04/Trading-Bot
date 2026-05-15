from datetime import datetime

from src.core.runtime import RuntimeState

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
    synchronize_transport_state
)
from datetime import timedelta


from src.core.events import (
    RuntimeEvent,
    RISK_ALERT,
    SYSTEM_RECALIBRATION,
)

from src.runtime.runtime_state_machine import (
    RuntimeStateMachine,
)

from src.runtime.runtime_metrics import (
    runtime_metrics,
)
from src.events.runtime_events import (
    RuntimeEventType,
)


from src.runtime.event_types import (
    EXECUTION_EVENT,
)

from src.runtime.logging.runtime_logger import (
    runtime_log,
)
from src.runtime.market_data_health import (
    MarketDataHealth,
)
from src.core.runtime_builder import (
    build_runtime_state,
)
class GovernedRuntime:

   

    def __init__(
        self,
        runtime_state: RuntimeState,
        event_bus: EventBus,
    ):

        if isinstance(
            runtime_state,
            RuntimeState,
        ):
            self.state = runtime_state

        else:
            self.state = build_runtime_state(
                capital=1000,
                timeframe="5m",
                adx_value=20,
                atr_percent=1.0,
            )

        self.event_bus = event_bus
        self.state_machine = (
            RuntimeStateMachine(
                self.state
            )
        )
        self.runtime_event_bus = (
            event_bus
        )
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
        self.event_bus.subscribe(
            EXECUTION_EVENT,
            self.handle_execution_event,
        )

    def start(self):

        self.state_machine.transition_to(
            RuntimeStatus.RUNNING,
            reason="Runtime start requested",
        )

        self.state.last_heartbeat = (
            datetime.utcnow()
        )

    def pause(self):

        self.state_machine.transition_to(
            RuntimeStatus.PAUSED,
            reason="Manual runtime pause",
        )

    def emergency_stop(
        self,
        reason: EmergencyReason,
    ):  
        if (
            self.state.status
            ==
            RuntimeStatus.EMERGENCY_STOP
        ):

            return

        self.state_machine.transition_to(
            RuntimeStatus.EMERGENCY_STOP,
            reason=(
                f"Emergency stop triggered: "
                f"{reason.value}"
            ),
        )

        self.state.emergency_reason = (
            reason
        )

        self.state.is_trading_enabled = (
            False
        )
        runtime_metrics[
            "emergency_stops"
        ] += 1

        event = RuntimeEvent(
            event_type=
            RuntimeEventType
            .EMERGENCY_STOP
            .value,

            payload={
                "reason":
                reason.value,

                "timestamp":
                datetime.utcnow()
                .isoformat(),
            },

            emitted_at=
            datetime.utcnow(),
        )

        self.runtime_event_bus.publish(
            event
        )
        
    def activate_safe_mode(
        self,
        reason: str,
    ):

        if self.state.safe_mode:
            return

        self.state.safe_mode = True

        runtime_log(
            level=LogLevel.WARNING,

            category=LogCategory.RUNTIME,

            message=(
                f"Safe mode activated: "
                f"{reason}"
            ),
        )
    def recover(self):

        self.state_machine.transition_to(
            RuntimeStatus.PAUSED,
            reason="Runtime recovery initiated",
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

        self.state_machine.transition_to(
            RuntimeStatus.COOLDOWN,
            reason="Cooldown activated",
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

           self.state_machine.transition_to(
                RuntimeStatus.PAUSED,
                reason="Cooldown completed",
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



    def validate_heartbeat(self):

        if heartbeat_expired(
            self.state
        ):

            self.emergency_stop(
                EmergencyReason
                .HEARTBEAT_FAILURE
            )

    def validate_market_data(self):
        synchronize_transport_state(
            self.state
        )

        if (
            not self.state.websocket_connected
        ):

            self.state.is_trading_enabled = False

            return

        if (
            self.state.last_tick_received_at
            is None
        ):

            return



    def execution_allowed(
        self,
    ) -> bool:

        return is_execution_allowed(
            self.state
        )

    def shutdown(self):

        self.state_machine.transition_to(
            RuntimeStatus.SHUTDOWN,
            reason="Runtime shutdown requested",
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

    def handle_execution_event(
        self,
        event_payload,
    ):

        runtime_log(
            level=LogLevel.INFO,

            category=LogCategory.EXECUTION,

            message=(
                f"Execution event received: "
                f"{event_payload}"
            ),
        )