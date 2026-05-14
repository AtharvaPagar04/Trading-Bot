from src.core.runtime_builder import (
    build_runtime_state,
)
from datetime import datetime

from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)



from src.market_data.market_tick import (
    MarketTick,
)

from src.market_data.market_data_router import (
    MarketDataRouter,
)


def test_market_tick_updates_runtime_heartbeat():

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

    router = MarketDataRouter(
        runtime
    )

    before = (
        runtime.market_data_health
        .last_update
    )

    tick = MarketTick(
        symbol="BTCUSDT",
        price=100000.0,
        timestamp=datetime.utcnow(),
        exchange="binance",
    )

    router.route_tick(
        tick
    )

    after = (
        runtime.market_data_health
        .last_update
    )

    assert after >= before