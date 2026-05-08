from datetime import datetime
from datetime import timedelta

from src.market.candle_feed_engine import (
    CandleFeedConfig,
    start_candle_feed_engine,
)

from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.market.market_data import (
    Candle,
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

base_time = datetime.utcnow()

incoming_candles = [
    Candle(
        timestamp=
        base_time
        + timedelta(minutes=i),

        open=120 + i,

        high=122 + i,

        low=118 + i,

        close=121 + i,

        volume=2000 + (i * 100),
    )
    for i in range(3)
]

config = CandleFeedConfig(
    interval_seconds=1
)

runtime = start_candle_feed_engine(
    runtime=runtime,

    snapshot=snapshot,

    candles=incoming_candles,

    config=config,
)