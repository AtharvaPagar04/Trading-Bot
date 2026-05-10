from datetime import (
    datetime,
    timedelta,
)

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

from src.paper_execution.order_status import (
    OrderStatus,
)


def test_pending_order_expires():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = (
        PaperExecutionEngine(
            runtime,

            max_fill_ratio=0.5,

            order_expiration_seconds=1,
        )
    )

    order = PaperOrder(
        symbol="BTCUSDT",

        side="BUY",

        quantity=0.05,

        price=100000.0,

        timestamp=(
            datetime.utcnow()
            -
            timedelta(seconds=5)
        ),
    )

    engine.execute_order(
        order
    )

    engine.process_pending_orders()

    assert (
        order.status
        ==
        OrderStatus.CANCELLED
    )

    assert (
        len(engine.pending_orders)
        ==
        0
    )