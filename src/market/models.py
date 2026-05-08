from dataclasses import dataclass

from src.market.candle_models import (
    Candle,
)


@dataclass
class MarketSnapshot:

    symbol: str

    timeframe: str

    close: float

    volume: float

    candles: list[Candle]