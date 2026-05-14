from src.core.runtime_builder import (
    build_runtime_state,
)
from datetime import datetime

from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)


from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.order_status import (
    OrderStatus,
)


def test_pending_order_progression():

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

    engine = (
        PaperExecutionEngine(
            runtime,

            max_fill_ratio=0.5,
        )
    )

    order = PaperOrder(
        symbol="BTCUSDT",

        side="BUY",

        quantity=0.05,

        price=100000.0,

        timestamp=datetime.utcnow(),
    )

    engine.execute_order(
        order
    )

    assert (
        order.status
        ==
        OrderStatus.PARTIALLY_FILLED
    )

    assert (
        len(engine.pending_orders)
        ==
        1
    )

    engine.process_pending_orders()

    assert (
        order.filled_quantity
        >
        0.025
    )