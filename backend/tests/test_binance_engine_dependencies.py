from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.execution.binance_execution_engine import (
    BinanceExecutionEngine,
)

from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_binance_engine_has_rest_client():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        EventBus(),
    )

    runtime.start()

    engine = (
        BinanceExecutionEngine(
            runtime
        )
    )

    assert isinstance(
        engine.rest_client,
        BinanceRestClient,
    )
