from src.core.runtime_builder import (
    build_runtime_state,
)
from datetime import datetime

from src.runtime.governed_runtime import (
    GovernedRuntime,
)
from src.paper_execution.portfolio_valuation import (
    calculate_total_equity,
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
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
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
        894.6
    )

def test_total_equity_calculation():

    runtime = GovernedRuntime(
    runtime_state=
    build_runtime_state(
        capital=1000,
        timeframe="5m",
        adx_value=20,
        atr_percent=1.0,
    ),

    event_bus=
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

    assert equity == 10885.5946