from src.core.runtime_builder import (
    build_runtime_state,
)
from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)



from src.execution.exchange_type import (
    ExchangeType,
)

from src.execution.execution_factory import (
    build_execution_engine,
)

from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)


def test_paper_engine_factory():

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
        build_execution_engine(
            ExchangeType.PAPER,
            runtime,
        )
    )

    assert isinstance(
        engine,
        PaperExecutionEngine,
    )
