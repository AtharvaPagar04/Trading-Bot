from datetime import datetime
from datetime import timedelta

from src.market.candle_models import (
    Candle,
)


class TimeframeAggregator:

    def __init__(
        self,
        interval_seconds: int = 60,
    ):

        self.interval_seconds = (
            interval_seconds
        )

        self.current_candle = None

        self.window_start = None

    def process_tick(
        self,
        price: float,
        quantity: float,
    ):

        now = datetime.utcnow()

        if self.current_candle is None:

            self.window_start = now

            self.current_candle = Candle(
                open=price,
                high=price,
                low=price,
                close=price,
                volume=quantity,
                timestamp=now,
            )

            return None

        elapsed = (
            now - self.window_start
        )

        candle = self.current_candle

        candle.high = max(
            candle.high,
            price,
        )

        candle.low = min(
            candle.low,
            price,
        )

        candle.close = price

        candle.volume += quantity

        if (
            elapsed >=
            timedelta(
                seconds=
                self.interval_seconds
            )
        ):

            completed = candle

            self.window_start = now

            self.current_candle = Candle(
                open=price,
                high=price,
                low=price,
                close=price,
                volume=quantity,
                timestamp=now,
            )

            return completed

        return None