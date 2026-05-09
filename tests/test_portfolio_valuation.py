from datetime import datetime

from src.runtime.governed_runtime import (
    GovernedRuntime,
)
from src.paper_execution.portfolio_valuation import (
    calculate_total_equity,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.runtime.event_bus import (
    EventBus,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)

from src.paper_execution.portfolio_valuation import (
    update_unrealized_pnl,
)


def test_unrealized_pnl_updates():

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
        quantity=0.09,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    engine.execute_order(
        buy_order
    )

    update_unrealized_pnl(
        portfolio=engine.portfolio,

        market_prices={
            "BTCUSDT": 110000.0,
        },
    )

    assert (
        engine.portfolio.unrealized_pnl
        ==
        900.0
    )

def test_total_equity_calculation():

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
        quantity=0.09,
        price=100000.0,
        timestamp=datetime.utcnow(),
    )

    engine.execute_order(
        buy_order
    )

    update_unrealized_pnl(
        portfolio=engine.portfolio,

        market_prices={
            "BTCUSDT": 110000.0,
        },
    )

    equity = (
        calculate_total_equity(
            portfolio=engine.portfolio,

            market_prices={
                "BTCUSDT": 110000.0,
            },
        )
    )

    assert equity == 10891.0