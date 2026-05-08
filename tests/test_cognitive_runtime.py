from datetime import datetime

from src.market.models import (
    MarketSnapshot,
)

from src.market.candle_models import (
    Candle,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.strategy_registry import (
    StrategyRegistry,
)

from src.strategy.performance_tracker import (
    StrategyPerformanceTracker,
)

from src.strategy.regime_router import (
    RegimeRouter,
)

from src.runtime.cognitive_runtime import (
    CognitiveRuntime,
)

registry = (
    StrategyRegistry()
)

registry.register(
    "mean_reversion",
    MeanReversionStrategy(),
)

tracker = (
    StrategyPerformanceTracker()
)

tracker.record_trade(
    "mean_reversion",
    10,
)

router = (
    RegimeRouter()
)

candles = []

prices = [
    100,
    101,
    102,
    103,
    104,
    105,
]

for price in prices:

    candles.append(
        Candle(
            open=price,
            high=price + 1,
            low=price - 1,
            close=price,
            volume=10,
            timestamp=
            datetime.utcnow(),
        )
    )

snapshot = (
    MarketSnapshot(
        symbol="BTCUSDT",

        timeframe="1m",

        close=105,

        volume=10,

        candles=candles,
    )
)

runtime = (
    CognitiveRuntime(
        registry,
        tracker,
        router,
    )
)

result = (
    runtime.process_market_snapshot(
        snapshot
    )
)

print()

print(
    "FINAL RESULT"
)

print(result)