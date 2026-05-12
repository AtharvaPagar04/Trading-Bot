from datetime import datetime
from datetime import datetime


class RuntimeController:

    def __init__(
        self,
    ):

        self.is_running = False

        self.is_paused = False

        self.safe_mode = False

        self.websocket = None

        self.runtime = None

        self.runtime_state = None

        self.exchange = None

        self.session_repository = None



    def __init__(
        self,
    ):

        self.is_running = False

        self.is_paused = False

        self.safe_mode = False

        self.websocket = None

        self.runtime = None

        self.runtime_state = None

        self.exchange = None

        self.session_repository = None

    def __init__(
        self,
    ):

        self.is_running = False

        self.is_paused = False

        self.safe_mode = False

        self.websocket = None

        self.runtime = None

        self.runtime_state = None

        self.exchange = None

        self.session_repository = None

    def start_runtime(
        self,
    ):

        if self.is_running:

            return

        self.is_running = True

        self.is_paused = False

        self.runtime_state.session_started_at = (
            datetime.utcnow()
        )

        session = (
            self.session_repository
            .create_session(
                started_at=
                self.runtime_state
                .session_started_at,
            )
        )

        self.runtime_state.active_session_id = (
            session.id
        )

        self.websocket.connect()

        print(
            f"[SESSION] "
            f"Started session "
            f"{session.id}"
        )

        print(
            "[SYSTEM] "
            "Live paper trading "
            "runtime started"
        )

    def stop_runtime(
        self,
    ):

        if not self.is_running:

            return

        self.is_running = False

        self.is_paused = False

        ended_at = (
            datetime.utcnow()
        )

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

                safe_mode_triggered=
                self.safe_mode,
            )

            print(
                f"[SESSION] "
                f"Ended session "
                f"{self.runtime_state.active_session_id}"
            )

        self.runtime_state.active_session_id = (
            None
        )

        self.websocket.disconnect()

        print(
            "[SYSTEM] "
            "Runtime stopped cleanly"
        )

    def pause_runtime(
        self,
    ):

        self.is_paused = True

    def resume_runtime(
        self,
    ):

        self.is_paused = False

    def enable_safe_mode(
        self,
    ):

        self.safe_mode = True

    def disable_safe_mode(
        self,
    ):

        self.safe_mode = False

    def register_runtime_resources(
        self,
        websocket,
        runtime,
        runtime_state,
        exchange,
        session_repository,
    ):

        self.websocket = websocket

        self.runtime = runtime

        self.runtime_state = runtime_state

        self.exchange = exchange

        self.session_repository = (
            session_repository
        )