from datetime import datetime

from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.market.market_data import (
    Candle,
)

from src.market.streaming_runtime import (
    process_incoming_candle,
)

from src.persistence.runtime_loader import (
    load_runtime_snapshot,
)

runtime = load_runtime_snapshot()

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

print("INITIAL CANDLES")
print(len(snapshot.candles))

new_candle = Candle(
    timestamp=
    datetime.utcnow(),

    open=120,

    high=125,

    low=118,

    close=124,

    volume=2500,
)

result = (
    process_incoming_candle(
        runtime=runtime,

        snapshot=snapshot,

        candle=new_candle,
    )
)

print("\nUPDATED CANDLES")
print(
    len(result.snapshot.candles)
)

print("\nLATEST CANDLE")
print(
    result.snapshot.candles[-1]
)

print("\nOPERATING STATE")
print(
    result.runtime
    .operating_state
)

print("\nMARKET STATE")
print(
    result.runtime
    .market_state
)
