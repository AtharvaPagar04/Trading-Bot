from datetime import datetime

from src.runtime.runtime_state import RuntimeState

from src.runtime.runtime_enums import (
    RuntimeMode,
    RuntimeStatus,
    EmergencyReason,
)

from src.runtime.event_bus import EventBus

from src.core.events import (
    RuntimeEvent,
    RISK_ALERT,
    SYSTEM_RECALIBRATION,
)

class GovernedRuntime:

    def __init__(
        self,
        mode: RuntimeMode,
        event_bus: EventBus,
    ):

        self.state = RuntimeState(mode=mode)

        self.event_bus = event_bus

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

        self.state.status = RuntimeStatus.RUNNING

        self.state.last_heartbeat = datetime.utcnow()

    def pause(self):

        self.state.status = RuntimeStatus.PAUSED

    def emergency_stop(
        self,
        reason: EmergencyReason,
    ):

        self.state.status = RuntimeStatus.EMERGENCY_STOP

        self.state.emergency_reason = reason

        self.state.is_trading_enabled = False

    def heartbeat(self):

        self.state.last_heartbeat = datetime.utcnow()

    def shutdown(self):

        self.state.status = RuntimeStatus.SHUTDOWN

    def handle_risk_alert(
        self,
        event: RuntimeEvent,
    ):

        severity = event.payload.get("severity")

        if severity == "critical":

            self.emergency_stop(
                EmergencyReason.MAX_DRAWDOWN,
            )

    def handle_recalibration(
        self,
        event: RuntimeEvent,
    ):

        self.pause()