from datetime import datetime
from datetime import datetime
from src.runtime.runtime_state_machine import (
    RuntimeStateMachine,
)

from src.runtime.runtime_enums import (
    RuntimeStatus,
)
from src.runtime.runtime_metrics import (
    runtime_metrics,
)
from src.events.runtime_events import (
    RuntimeEventType,
    RuntimeStartedEvent,
    RuntimePausedEvent,
    RuntimeRecoveredEvent,
    SessionStartedEvent,
    SessionStoppedEvent,
    TradingEnabledEvent,
    TradingDisabledEvent,
    SafeModeTriggeredEvent,
)
from src.runtime.logging.runtime_loggers import (
    runtime_logger,
    session_logger,
    governance_logger,
    recovery_logger,
)

class RuntimeController:




    def __init__(
        self,
    ):

        self.state_machine = None

        self.websocket = None

        self.runtime = None

        self.runtime_state = None

        self.exchange = None

        self.session_repository = None
        self.event_bus = None

    def start_runtime(
        self,
    ):

        if self.state_machine is None:

            return

        if self.state_machine.is_running():

            return

        self.state_machine.transition_to(
            RuntimeStatus.RUNNING,
            reason="Runtime start requested",
        )

        self.websocket.connect()

        if self.event_bus is not None:
            self.event_bus.publish(
                RuntimeStartedEvent(
                    event_type="runtime_started",
                    emitted_at=datetime.utcnow(),
                )
            )

        runtime_logger.info(
            "Live paper trading runtime started"
        )

    def stop_runtime(
        self,
    ):

        if not self.state_machine.is_running():

            return

        self.state_machine.transition_to(
            RuntimeStatus.PAUSED,
            reason="Runtime stop requested",
        )

        ended_at = (
            datetime.utcnow()
        )

        duration_seconds = 0

        if (
            self.runtime_state
            .session_started_at
            is not None
        ):

            duration_seconds = int(
        (
            ended_at
            -
            self.runtime_state
            .session_started_at
        ).total_seconds()
    )

        portfolio_value = (
            self.exchange.balance
            .available_capital
        )

        if (
            self.runtime_state.latest_price
            is not None
        ):

            for position in (
                self.exchange.positions
                .values()
            ):

                portfolio_value += (
                    position.quantity
                    *
                    self.runtime_state
                    .latest_price
                )

        if (
            self.runtime_state
            .active_session_id
            is not None
        ):

            self.session_repository.end_session(
                session_id=
                self.runtime_state
                .active_session_id,

                ended_at=
                ended_at,

                duration_seconds=
                duration_seconds,

                total_trades=
                self.runtime_state
                .total_trades,

                realized_pnl=
                self.runtime_state
                .current_unrealized_pnl,

                portfolio_value=
                portfolio_value,

                
            )

            session_logger.info(
                f"Ended session "
                f"{self.runtime_state.active_session_id}"
            )

        self.runtime_state.active_session_id = (
            None
        )
        
        self.runtime_state.is_trading_enabled = (
            False
        )
        
        self.websocket.disconnect()

        runtime_logger.info(
            "Runtime stopped cleanly"
        )

    def pause_runtime(
        self,
    ):

        self.state_machine.transition_to(
            RuntimeStatus.PAUSED,
            reason="Manual runtime pause",
        )
        if self.event_bus is not None:
            self.event_bus.publish(
                RuntimePausedEvent(
                    event_type="runtime_paused",
                    emitted_at=datetime.utcnow(),
                    reason="Manual runtime pause",
                )
            )

    def resume_runtime(
        self,
    ):

       self.state_machine.transition_to(
            RuntimeStatus.RUNNING,
            reason="Runtime resume requested",
        )
        
    def is_running(
    self,
    ) -> bool:

        if self.state_machine is None:
            return False

        return (
            self.state_machine
            .is_running()
        )


    def is_paused(
        self,
    ) -> bool:

        if self.state_machine is None:
            return False

        return (
            self.state_machine
            .is_paused()
        )

    @property
    def safe_mode(
        self,
    ) -> bool:

        if self.runtime_state is None:
            return False

        return (
            self.runtime_state.safe_mode
        )


    def is_shutdown(
        self,
    ) -> bool:

        if self.state_machine is None:
            return False

        return (
            self.state_machine
            .is_shutdown()
        )
         
    def enable_safe_mode(
        self,
    ):

        self.runtime_state.safe_mode = (
            True
        )

        runtime_metrics[
            "safe_mode_activations"
        ] += 1
        
        if self.event_bus is not None:

            self.event_bus.publish(
                SafeModeTriggeredEvent(
                    event_type="safe_mode_triggered",
                    emitted_at=datetime.utcnow(),
                )
            )
        
        if self.state_machine is None:

            return

        self.state_machine.transition_to(
            RuntimeStatus.SAFE_MODE,
            reason="Safe mode activated",
        )
        
    def disable_safe_mode(
        self,
    ):

        self.state_machine.transition_to(
            RuntimeStatus.RUNNING,
            reason="Safe mode disabled",
        )

        self.runtime_state.safe_mode = False

    def enable_trading(self):

        if self.runtime_state is None:
            raise RuntimeError(
                "Runtime not initialized"
            )

        self.runtime_state.is_trading_enabled = True

        if self.event_bus is not None:
            self.event_bus.publish(
                TradingEnabledEvent(
                    event_type="trading_enabled",
                    emitted_at=datetime.utcnow(),
                )
            )

    def disable_trading(self):

        if self.runtime_state is None:
            raise RuntimeError(
                "Runtime not initialized"
            )

        self.runtime_state.is_trading_enabled = False

        if self.event_bus is not None:
            self.event_bus.publish(
                TradingDisabledEvent(
                    event_type="trading_disabled",
                    emitted_at=datetime.utcnow(),
                    reason="Manual disable",
                )
            )

    def emergency_stop(self, reason: str = "Manual emergency stop") -> None:
        from src.runtime.runtime_enums import EmergencyReason
        self.runtime_state.emergency_reason = EmergencyReason.MANUAL_STOP
        self.runtime_state.is_trading_enabled = False
        self.state_machine.transition_to(
            RuntimeStatus.EMERGENCY_STOP,
            reason=reason,
        )

    def start_session(self) -> dict:
        """
        Start a trading session independently of the runtime lifecycle.
        Requires: runtime RUNNING, trading enabled, no active session.
        """
        if self.state_machine is None:
            raise RuntimeError("Runtime not initialized")

        if not self.state_machine.is_running():
            raise RuntimeError(
                f"Cannot start session: runtime is {self.runtime_state.status.value}"
            )

        if self.runtime_state.safe_mode:
            raise RuntimeError("Cannot start session: safe mode is active")

        if not self.runtime_state.is_trading_enabled:
            raise RuntimeError("Cannot start session: trading is disabled by governance")

        if self.runtime_state.active_session_id is not None:
            raise RuntimeError(
                f"Session {self.runtime_state.active_session_id} already active"
            )

        started_at = datetime.utcnow()
        self.runtime_state.session_started_at = started_at

        session = self.session_repository.create_session(started_at=started_at)
        self.runtime_state.active_session_id = session.id

        if self.event_bus is not None:
            self.event_bus.publish(
                SessionStartedEvent(
                    event_type="session_started",
                    emitted_at=datetime.utcnow(),
                    session_id=session.id,
                    started_at=started_at,
                )
            )

        session_logger.info(f"Started session {session.id}")
        return {"session_id": session.id, "started_at": started_at.isoformat()}

    def stop_session(self) -> dict:
        """
        Stop the active trading session without altering runtime lifecycle state.
        """
        if self.runtime_state is None:
            raise RuntimeError("Runtime not initialized")

        session_id = self.runtime_state.active_session_id
        if session_id is None:
            raise RuntimeError("No active session to stop")

        ended_at = datetime.utcnow()
        duration_seconds = 0
        if self.runtime_state.session_started_at is not None:
            duration_seconds = int(
                (ended_at - self.runtime_state.session_started_at).total_seconds()
            )

        portfolio_value = float(self.exchange.balance.available_capital)
        if self.runtime_state.latest_price is not None:
            for position in self.exchange.positions.values():
                portfolio_value += position.quantity * self.runtime_state.latest_price

        self.session_repository.end_session(
            session_id=session_id,
            ended_at=ended_at,
            duration_seconds=duration_seconds,
            total_trades=self.runtime_state.total_trades,
            realized_pnl=self.runtime_state.current_unrealized_pnl,
            portfolio_value=portfolio_value,
            safe_mode_triggered=self.runtime_state.safe_mode,
        )

        self.runtime_state.active_session_id = None
        self.runtime_state.session_started_at = None
        self.runtime_state.total_trades = 0

        if self.event_bus is not None:
            self.event_bus.publish(
                SessionStoppedEvent(
                    event_type="session_stopped",
                    emitted_at=datetime.utcnow(),
                    session_id=session_id,
                    stopped_at=ended_at,
                    duration_seconds=duration_seconds,
                )
            )

        session_logger.info(f"Stopped session {session_id}")
        return {"session_id": session_id, "ended_at": ended_at.isoformat()}

    def get_session_status(self) -> dict:
        """Return the current session lifecycle status."""
        if self.runtime_state is None:
            return {"session_active": False, "blocked": True, "reason": "Runtime not initialized"}

        active_id = self.runtime_state.active_session_id
        status = self.runtime_state.status.value

        # Determine blocking conditions
        blocking_states = {"safe_mode", "emergency_stop", "cooldown", "paused", "shutdown", "starting"}
        blocked = status in blocking_states or not self.runtime_state.is_trading_enabled

        reason = None
        if status in blocking_states:
            reason = f"Session blocked: runtime in {status}"
        elif not self.runtime_state.is_trading_enabled:
            reason = "Session blocked: trading disabled by governance"

        result: dict = {
            "session_active": active_id is not None,
            "active_session_id": active_id,
            "session_started_at": (
                self.runtime_state.session_started_at.isoformat()
                if self.runtime_state.session_started_at else None
            ),
            "total_trades": self.runtime_state.total_trades,
            "session_pnl": self.runtime_state.session_pnl,
            "runtime_status": status,
            "trading_enabled": self.runtime_state.is_trading_enabled,
            "blocked": blocked,
            "reason": reason,
        }
        return result

    def recover_runtime(self):
        if self.runtime_state is None:
            raise RuntimeError("Runtime not initialized")

        if self.runtime_state.status != RuntimeStatus.EMERGENCY_STOP:
            raise RuntimeError(f"Recovery not applicable in state: {self.runtime_state.status.value}")

        previous_state = self.runtime_state.status.value

        self.state_machine.transition_to(
            RuntimeStatus.PAUSED,
            reason="Manual recovery initiated",
        )
        self.runtime_state.emergency_reason = None
        self.runtime_state.is_trading_enabled = False

        if self.event_bus is not None:
            self.event_bus.publish(
                RuntimeRecoveredEvent(
                    event_type="runtime_recovered",
                    emitted_at=datetime.utcnow(),
                    previous_state=previous_state,
                )
            )

    def shutdown_runtime(self) -> None:

        self.runtime_state.is_trading_enabled = False
        self.state_machine.transition_to(
            RuntimeStatus.SHUTDOWN,
            reason="Manual shutdown requested",
        )

    def register_runtime_resources(
        self,
        websocket,
        runtime,
        runtime_state,
        exchange,
        session_repository,
        event_bus,
    ):

        self.websocket = websocket

        self.runtime = runtime
        self.event_bus = event_bus

        self.runtime_state = runtime_state
        self.state_machine = (
            RuntimeStateMachine(
                runtime_state
            )
        )

        self.exchange = exchange

        self.session_repository = (
            session_repository
        )