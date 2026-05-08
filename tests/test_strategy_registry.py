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

from src.strategy.orchestrator import (
    StrategyOrchestrator,
)

from datetime import datetime

registry = (
    StrategyRegistry()
)

registry.register(
    "mean_reversion",
    MeanReversionStrategy(),
)

snapshot = (
    MarketSnapshot(
        symbol="BTCUSDT",

        timeframe="1m",

        close=100,

        volume=10,

        candles=[
            Candle(
                open=100,
                high=101,
                low=99,
                close=100,
                volume=10,
                timestamp=
                datetime.utcnow(),
            )
        ] * 20,
    )
)

orchestrator = (
    StrategyOrchestrator(
        registry
    )
)

decision = (
    orchestrator.evaluate(
        snapshot
    )
)

print()

print(
    "FINAL DECISION"
)

print(decision)