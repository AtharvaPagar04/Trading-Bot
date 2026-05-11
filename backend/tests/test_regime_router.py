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

from src.strategy.regime_adaptive_orchestrator import (
    RegimeAdaptiveOrchestrator,
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
    RegimeAdaptiveOrchestrator(
        registry,
        tracker,
        router,
    )
)

decision = (
    orchestrator.evaluate(
        snapshot,
        regime="RANGE",
    )
)

print()

print(
    "FINAL REGIME DECISION"
)

print(decision)