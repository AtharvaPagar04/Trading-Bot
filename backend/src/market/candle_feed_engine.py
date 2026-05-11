import time
from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)

from src.market.streaming_runtime import (
    process_incoming_candle,
)


@dataclass
class CandleFeedConfig:
    interval_seconds: int


def start_candle_feed_engine(
    runtime: RuntimeState,

    snapshot: MarketDataSnapshot,

    candles: list[Candle],

    config: CandleFeedConfig,
) -> RuntimeState:

    for index, candle in enumerate(
        candles
    ):

        print(
            f"\n===== "
            f"CANDLE TICK "
            f"{index + 1}"
            f" ====="
        )

        result = (
            process_incoming_candle(
                runtime=runtime,

                snapshot=snapshot,

                candle=candle,
            )
        )

        runtime = result.runtime

        print(
            "OPERATING STATE:",
            runtime.operating_state,
        )

        print(
            "ATR:",
            runtime.market_state
            .atr_percent,
        )

        print(
            "ADX:",
            runtime.market_state
            .adx,
        )

        print(
            "EVENT COUNT:",
            len(
                runtime.active_events
            ),
        )

        time.sleep(
            config.interval_seconds
        )

    return runtime