import pandas as pd

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)


def load_market_snapshot_from_csv(
    filepath: str,

    symbol: str,

    timeframe: str,
) -> MarketDataSnapshot:

    df = pd.read_csv(
        filepath,
        parse_dates=["timestamp"],
    )

    candles = []

    for _, row in df.iterrows():

        candles.append(
            Candle(
                timestamp=
                row["timestamp"],

                open=row["open"],

                high=row["high"],

                low=row["low"],

                close=row["close"],

                volume=row["volume"],
            )
        )

    return MarketDataSnapshot(
        symbol=symbol,

        timeframe=timeframe,

        candles=candles,
    )