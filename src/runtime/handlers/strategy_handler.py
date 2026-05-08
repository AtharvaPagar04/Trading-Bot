from src.market.models import (
    MarketSnapshot,
)

from src.market.timeframe_aggregator import (
    TimeframeAggregator,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.models import (
    TradeSignal,
)

from src.runtime.handlers.execution_handler import (
    handle_execution_signal,
)

strategy = (
    MeanReversionStrategy()
)

aggregator = (
    TimeframeAggregator(
        interval_seconds=10
    )
)

candles = []


async def handle_strategy_event(
    event,
):

    payload = event.payload

    completed_candle = (
        aggregator.process_tick(
            price=
            payload["price"],

            quantity=
            payload["quantity"],
        )
    )

    if completed_candle is None:

        return

    candles.append(
        completed_candle
    )

    snapshot = (
        MarketSnapshot(
            symbol=
            payload["symbol"],

            timeframe="10s",

            close=
            completed_candle.close,

            volume=
            completed_candle.volume,

            candles=
            candles[-50:],
        )
    )

    signal = (
        strategy.generate_signal(
            snapshot
        )
    )

    print(
        "LIVE SIGNAL"
    )

    print(signal)

    if (
        signal.signal
        !=
        TradeSignal.HOLD
    ):

        await (
            handle_execution_signal(
                signal
            )
        )