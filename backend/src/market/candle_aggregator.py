from datetime import datetime

from src.market.candle_models import (
    Candle,
)


class CandleAggregator:

    def __init__(self):

        self.current_candle = None

    def process_tick(
        self,
        price: float,
        quantity: float,
    ):

        now = datetime.utcnow()

        if self.current_candle is None:

            self.current_candle = Candle(
                open=price,

                high=price,

                low=price,

                close=price,

                volume=quantity,

                timestamp=now,
            )

            return self.current_candle

        candle = (
            self.current_candle
        )

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

        return candle