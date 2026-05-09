from datetime import datetime

from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
    EmergencyReason,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)


def test_paper_order_executes():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = PaperExecutionEngine(
        runtime
    )

    order = PaperOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.01,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        order
    )

    assert result is True

    assert (
        len(engine.executed_orders)
        == 1
    )


def test_execution_blocked_during_emergency():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    runtime.emergency_stop(
        EmergencyReason
        .HEARTBEAT_FAILURE
    )

    engine = PaperExecutionEngine(
        runtime
    )

    order = PaperOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.01,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        order
    )

    assert result is False

    assert (
        len(engine.executed_orders)
        == 0
    )

def test_buy_order_updates_portfolio():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = PaperExecutionEngine(
        runtime
    )

    starting_balance = (
        engine.portfolio.cash_balance
    )

    order = PaperOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.01,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        order
    )

    assert result is True

    assert (
        engine.portfolio.cash_balance
        ==
        starting_balance - 1000.0
    )

    assert (
        engine.portfolio.positions[
            "BTCUSDT"
        ]
        ==
        0.01
    )


def test_order_rejected_for_insufficient_balance():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = PaperExecutionEngine(
        runtime
    )

    order = PaperOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=100.0,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        order
    )

    assert result is False

    assert (
        len(engine.executed_orders)
        == 0
    )

def test_sell_order_reduces_position():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = PaperExecutionEngine(
        runtime
    )

    buy_order = PaperOrder(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.02,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    engine.execute_order(
        buy_order
    )

    starting_balance = (
        engine.portfolio.cash_balance
    )

    sell_order = PaperOrder(
        symbol="BTCUSDT",
        side="SELL",
        quantity=0.01,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        sell_order
    )

    assert result is True

    assert (
        engine.portfolio.positions[
            "BTCUSDT"
        ]
        ==
        0.01
    )

    assert (
        engine.portfolio.cash_balance
        ==
        starting_balance + 1000.0
    )


def test_sell_rejected_for_insufficient_position():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = PaperExecutionEngine(
        runtime
    )

    sell_order = PaperOrder(
        symbol="BTCUSDT",
        side="SELL",
        quantity=1.0,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    result = engine.execute_order(
        sell_order
    )

    assert result is False