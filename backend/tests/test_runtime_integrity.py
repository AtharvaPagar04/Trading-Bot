from src.runtime.runtime_controller import (
    RuntimeController,
)
from src.runtime.live_tick_handler import (
    LiveTickHandler,
)

from src.market_data.market_tick import (
    MarketTick,
)
from src.runtime.runtime_enums import (
    RuntimeStatus,
)
from src.core.event_bus import (
    EventBus,
)

from datetime import datetime

class MockExchange:

    def portfolio_reconciliation_valid(
        self,
        latest_price: float,
    ) -> bool:

        return False


def test_reconciliation_failure_triggers_safe_mode():

    controller = RuntimeController()

    controller.runtime_state = type(
        "RuntimeState",
        (),
        {
            "safe_mode": False,
        },
    )()

    controller.enable_safe_mode()

    assert (
        controller.runtime_state
        .safe_mode
        is True
    )

class MockExchange:

    positions = {}

    def portfolio_reconciliation_valid(
        self,
        latest_price: float,
    ) -> bool:

        return False


class MockRuntimeController:
    def is_running(
        self,
    ):
        return True

    def __init__(self):

        self.safe_mode_enabled = (
            False
        )

    def enable_safe_mode(
        self,
    ):

        self.safe_mode_enabled = (
            True
        )


class MockRuntimeState:

    latest_price = 0.0

    last_tick_received_at = None
    status = RuntimeStatus.RUNNING

    session_started_at = (
        datetime.utcnow()
    )

    runtime_uptime_seconds = 0

    latest_candle_close = 0.0

    latest_candle_timestamp = None

    current_unrealized_pnl = 0.0

    current_unrealized_pnl_percent = (
        0.0
    )

    operating_state = "RUNNING"

    safe_mode = False

    total_trades = 0


def test_tick_processing_triggers_safe_mode_on_reconciliation_failure():

    runtime_state = (
        MockRuntimeState()
    )

    exchange = (
        MockExchange()
    )

    controller = (
        MockRuntimeController()
    )

    handler = LiveTickHandler(
        runtime_state=
        runtime_state,

        exchange=
        exchange,

        runtime_controller=
        controller,
        event_bus=EventBus(),
    )

    tick = MarketTick(
        symbol="BTCUSDT",

        price=50000.0,

        timestamp=
        datetime.utcnow(),

        exchange="BINANCE",
    )

    handler.process_tick(
        tick
    )
    assert (
        runtime_state.latest_price
        == 50000.0
    )