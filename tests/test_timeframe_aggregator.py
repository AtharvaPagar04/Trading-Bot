import time

from src.market.timeframe_aggregator import (
    TimeframeAggregator,
)

aggregator = (
    TimeframeAggregator(
        interval_seconds=5
    )
)

prices = [
    100,
    101,
    99,
    102,
    101,
    103,
]

for price in prices:

    candle = (
        aggregator.process_tick(
            price=price,
            quantity=1.0,
        )
    )

    if candle:

        print(
            "COMPLETED CANDLE"
        )

        print(candle)

    time.sleep(1)