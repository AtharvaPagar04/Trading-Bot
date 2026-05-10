from datetime import datetime

from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)


def test_latency_blocks_fill_progression():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = (
        PaperExecutionEngine(
            runtime,

            max_fill_ratio=0.5,

            execution_latency_seconds=60,
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

    initial_fill = (
        order.filled_quantity
    )

    engine.process_pending_orders()

    assert (
        order.filled_quantity
        ==
        initial_fill
    )