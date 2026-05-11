from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    volume: float


@dataclass
class MarketDataSnapshot:
    symbol: str

    timeframe: str

    candles: list[Candle]