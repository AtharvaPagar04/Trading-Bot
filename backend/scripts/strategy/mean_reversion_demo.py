from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.strategy.mean_reversion import (
    generate_mean_reversion_signal,
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

signal = (
    generate_mean_reversion_signal(
        snapshot
    )
)

print(signal)