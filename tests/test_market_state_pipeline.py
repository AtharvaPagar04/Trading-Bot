from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.market.market_state_pipeline import (
    generate_market_state,
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

market_state = (
    generate_market_state(
        snapshot
    )
)

print(market_state)