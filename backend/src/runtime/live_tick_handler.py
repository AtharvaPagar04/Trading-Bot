from datetime import datetime
import time

from src.market_data.market_tick import (
    MarketTick,
)

from src.runtime.runtime_console_renderer import (
    render_runtime_snapshot,
)

from src.runtime.runtime_registry import (
    runtime_snapshot,
)

from src.core.autonomous_runtime import (
    execute_autonomous_cycle,
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

from src.exchange.models import (
    OrderSide,
)

from src.db.runtime_repository import (
    RuntimeRepository,
)
from datetime import (
    datetime,
)

class LiveTickHandler:

    def __init__(
        self,
        runtime_state,
        exchange,
        runtime_controller,
    ):

        self.runtime_state = (
            runtime_state
        )
        self.runtime_repository = (
            RuntimeRepository()
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
        self.runtime_controller = (
            runtime_controller
        )

    def process_tick(
        self,
        tick: MarketTick,
    ):
        if (
            not
            self.runtime_controller
            .is_running
        ):

            return
            
        self.runtime_state.latest_price = (
            tick.price
        )

        self.runtime_state.runtime_uptime_seconds = int(
        (
            datetime.utcnow()
            -
            self.runtime_state
            .session_started_at
        ).total_seconds()
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

           

            if pnl_percent >= -0.35:

                self.exchange.execute_market_order(
                    symbol=tick.symbol,

                    side=OrderSide.SELL,

                    quantity=position.quantity,

                    price=tick.price,
                )

                print(
                    f"[SELL] "
                    f"{tick.symbol} "
                    f"Profit Target Hit"
                )

                return

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

        if (
            self.runtime_controller
            .is_paused
        ):

            return

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
        self.runtime_repository.save_runtime_state(
            operating_state=
                self.runtime_state
                .operating_state,

            safe_mode=
                self.runtime_state
                .safe_mode,

            total_trades=
                self.runtime_state
                .total_trades,
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

                runtime_controller=
                self.runtime_controller,
            )
        )

        runtime_snapshot.clear()

        runtime_snapshot.update(
            snapshot_data
        )

        render_runtime_snapshot(
            snapshot_data
        )
        
    def load_persisted_runtime_state(
        self,
    ):

        persisted_runtime = (
            self.runtime_repository
            .load_runtime_state()
        )

        if persisted_runtime:

            self.runtime_state.operating_state = (
                persisted_runtime
                .operating_state
            )

            self.runtime_state.safe_mode = (
                persisted_runtime
                .safe_mode
            )

            self.runtime_state.total_trades = (
                persisted_runtime
                .total_trades
            )

            print(
                "[RECOVERY] "
                "Runtime state restored"
            )