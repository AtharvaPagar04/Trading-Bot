from datetime import datetime

from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.market_data.market_tick import (
    MarketTick,
)

from src.market_data.market_data_router import (
    MarketDataRouter,
)


def test_market_tick_updates_runtime_heartbeat():

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
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