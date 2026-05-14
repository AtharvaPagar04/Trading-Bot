from src.core.runtime_builder import (
    build_runtime_state,
)
from src.core.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)



from src.execution.binance_execution_engine import (
    BinanceExecutionEngine,
)

from src.exchange.binance_rest_client import (
    BinanceRestClient,
)


def test_binance_engine_has_rest_client():

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
        BinanceExecutionEngine(
            runtime
        )
    )

    assert isinstance(
        engine.rest_client,
        BinanceRestClient,
    )
