from src.runtime.metrics import (
    RuntimeMetrics,
)

metrics = (
    RuntimeMetrics()
)

metrics.increment(
    "market_ticks"
)

metrics.increment(
    "market_ticks"
)

metrics.increment(
    "signals_generated"
)

metrics.increment(
    "execution_attempts"
)

metrics.increment(
    "execution_attempts"
)

metrics.increment(
    "execution_attempts"
)

print()

print(
    "MARKET TICKS"
)

print(
    metrics.get_metric(
        "market_ticks"
    )
)

print()

print(
    "FULL REPORT"
)

print(
    metrics.report()
)