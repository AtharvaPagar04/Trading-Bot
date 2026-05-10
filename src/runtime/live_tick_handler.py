import time

from src.market_data.market_tick import (
    MarketTick,
)
from src.runtime.runtime_console_renderer import (
    render_runtime_snapshot,
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
from src.market.timeframe_aggregator import (
    TimeframeAggregator,
)
from src.runtime.runtime_snapshot import (
    build_runtime_snapshot,
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
        self.last_pnl_log_time = 0
        self.aggregator = (
            TimeframeAggregator(
                interval_seconds=60
            )
        )

    def process_tick(
        self,
        tick: MarketTick,
    ):

        

        self.runtime_state.latest_price = (
            tick.price
        )
        completed_candle = (
            self.aggregator.process_tick(
                price=tick.price,

                quantity=0,
            )
        )
        
        



        if (
            tick.symbol
            in self.exchange.positions
        ):

            position = (
                self.exchange.positions[
                    tick.symbol
                ]
            )

            pnl_percent = (
                (
                    tick.price
                    -
                    position.average_price
                )
                /
                position.average_price
            ) * 100
            self.runtime_state.current_unrealized_pnl_percent = (
                pnl_percent
            )

            position_value = (
                tick.price
                *
                position.quantity
            )

            entry_value = (
                position.average_price
                *
                position.quantity
            )

            self.runtime_state.current_unrealized_pnl = (
                position_value
                -
                entry_value
            )

            

            

                

            if pnl_percent >= 0.2:

                self.exchange.execute_market_order(
                    symbol=tick.symbol,

                    side=OrderSide.SELL,

                    quantity=position.quantity,

                    price=tick.price,
                )

                print(
                    f'[SELL] '
                    f'{tick.symbol} '
                    f'Profit Target Hit'
                )

            
        if completed_candle is None:

            return
        self.runtime_state.latest_candle_close = (
            completed_candle.close
        )

        self.runtime_state.latest_candle_timestamp = (
            completed_candle.timestamp
        )
        print(
            f"[CANDLE CLOSED] "
            f"O={completed_candle.open} "
            f"H={completed_candle.high} "
            f"L={completed_candle.low} "
            f"C={completed_candle.close}"
        )
        snapshot = (
            MarketDataSnapshot(
                symbol=tick.symbol,

                timeframe="1m",

                candles=[completed_candle],
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
                completed_candle,

                trade_side=
                "BUY",
            )
        )

        self.runtime_state = (
            result.runtime
        )
        if result.executed:

            self.runtime_state.total_trades += 1

            self.runtime_state.last_execution_price = (
                tick.price
            )

            self.runtime_state.last_execution_time = (
                tick.timestamp
            )

        

        
        

        
        snapshot_data = (
            build_runtime_snapshot(
                runtime=
                self.runtime_state,
                exchange=
                self.exchange,
            )
        )
        render_runtime_snapshot(
            snapshot_data
        )
        