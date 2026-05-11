from src.strategy.performance_tracker import (
    StrategyPerformanceTracker,
)

tracker = (
    StrategyPerformanceTracker()
)

tracker.record_trade(
    strategy_name=
    "mean_reversion",

    pnl=10,
)

tracker.record_trade(
    strategy_name=
    "mean_reversion",

    pnl=-5,
)

tracker.record_trade(
    strategy_name=
    "trend_following",

    pnl=20,
)

print()

print(
    "MEAN REVERSION"
)

print(
    tracker.get_stats(
        "mean_reversion"
    )
)

print()

print(
    "FULL REPORT"
)

print(
    tracker.full_report()
)