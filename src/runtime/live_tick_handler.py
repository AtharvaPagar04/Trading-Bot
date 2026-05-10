from src.market_data.market_tick import (
    MarketTick,
)



from src.core.autonomous_runtime import (
    execute_autonomous_cycle,
)
from src.market.market_data import (
    Candle,
)
from src.market.market_data import (
    Candle,
    MarketDataSnapshot,
)


class LiveTickHandler:

    def __init__(
        self,
        runtime_state,
        exchange,
    ):

        self.runtime_state = (
            runtime_state
        )

        self.exchange = (
            exchange
        )

    def process_tick(
        self,
        tick: MarketTick,
    ):

        candle = Candle(
            timestamp=tick.timestamp,

            open=tick.price,

            high=tick.price,

            low=tick.price,

            close=tick.price,

            volume=0,
        )

        snapshot = (
            MarketDataSnapshot(
                symbol=tick.symbol,

                timeframe="1m",

                candles=[candle],
            )
        )

    

        result = (
            execute_autonomous_cycle(
                runtime=
                self.runtime_state,

                exchange=
                self.exchange,

                snapshot=
                snapshot,

                candle=
                candle,

                trade_side=
                "BUY",
            )
        )

        self.runtime_state = (
            result.runtime
        )

        print(
            f'[LIVE] '
            f'{tick.symbol} '
            f'Price={tick.price}'
        )

        print(
            f'[EXECUTED] '
            f'{result.executed}'
        )