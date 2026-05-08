from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

print(snapshot.symbol)

print(snapshot.timeframe)

print(
    len(snapshot.candles)
)

print(
    snapshot.candles[0]
)