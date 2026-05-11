from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
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
        RuntimeMode.DRY_RUN,
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
