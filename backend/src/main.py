import time
import uvicorn
import threading
from datetime import datetime
from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.runtime.runtime_enums import (
    RuntimeMode,
)

from src.market_data.market_data_router import (
    MarketDataRouter,
)

from src.exchange.binance_websocket_client import (
    BinanceWebSocketClient,
)

from src.runtime.live_tick_handler import (
    LiveTickHandler,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)
from src.core.runtime_builder import (
    build_runtime_state,
)
from src.api.main import (
    runtime_controller,
)
from src.db.trading_session_repository import (
    TradingSessionRepository,
)
from src.runtime.runtime_monitor import (
    RuntimeMonitor,
)

from src.runtime.runtime_monitor_loop import (
    RuntimeMonitorLoop,
)
def main():

    event_bus = EventBus()

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        event_bus,
    )

    runtime.start()

    
    runtime_monitor = (
        RuntimeMonitor(
            runtime=runtime,
        )
    )

    runtime_monitor_loop = (
        RuntimeMonitorLoop(
            monitor=runtime_monitor,
        )
    )

    runtime_monitor_loop.start()
   

    runtime_state = (
        build_runtime_state(
            capital=2000,

            timeframe="5m",

            adx_value=20,

            atr_percent=1.5,
        )
    )

    api_thread = threading.Thread(
        target=lambda: uvicorn.run(
            "src.api.main:app",
            host="0.0.0.0",
            port=8000,
            reload=False,
        ),
        daemon=True,
    )

    api_thread.start()

    session_repository = (
        TradingSessionRepository()
    )

    recovered_sessions = (
        session_repository
        .recover_orphan_sessions()
    )

    if recovered_sessions > 0:

        print(
            f"[RECOVERY] "
            f"Recovered "
            f"{recovered_sessions} "
            f"orphan sessions"
        )


    exchange = (
        PaperExchange(
            starting_capital=2000,

            active_session_id=
                runtime_state
                .active_session_id,
        )
    )
    exchange.load_persisted_positions()
    
    tick_handler = (
        LiveTickHandler(
            runtime_state=
            runtime_state,

            exchange=
            exchange,

            runtime_controller=
            runtime_controller,
        )
    )
    exchange.load_persisted_balance()
    

    router = (
        MarketDataRouter(
            runtime=
            runtime,

            tick_handler=
            tick_handler,
        )
    )

    websocket = (
        BinanceWebSocketClient(
            router=
            router,

            symbol="btcusdt",
        )
    )
    runtime_controller.register_runtime_resources(
        websocket=websocket,
        runtime=runtime,
        runtime_state=runtime_state,
        exchange=exchange,
        session_repository=session_repository,
    )
   

    try:

        while True:
            if (
                runtime_state
                .active_session_id
                is not None
            ):

                current_time = (
                    datetime.utcnow()
                )

                duration_seconds = int(
                    (
                        current_time
                        -
                        runtime_state
                        .session_started_at
                    )
                    .total_seconds()
                )

                portfolio_value = (
                    exchange.balance
                    .available_capital
                )

                if (
                    runtime_state.latest_price
                    is not None
                ):

                    for position in (
                        exchange.positions
                        .values()
                    ):

                        portfolio_value += (
                            position.quantity
                            *
                            runtime_state
                            .latest_price
                        )

                session_repository.update_live_session(
                    session_id=
                        runtime_state
                        .active_session_id,

                    duration_seconds=
                        duration_seconds,

                    total_trades=
                        runtime_state
                        .total_trades,

                    realized_pnl=
                        runtime_state
                        .current_unrealized_pnl,

                    portfolio_value=
                        portfolio_value,
                )
        

            time.sleep(1)

    except KeyboardInterrupt:

        print(
            "\n[SYSTEM] "
            "Shutdown requested"
        )
        if (
            runtime_state.active_session_id
            is not None
        ):

            ended_at = (
                datetime.utcnow()
            )

            duration_seconds = int(
                (
                    ended_at
                    -
                    runtime_state
                    .session_started_at
                ).total_seconds()
            )

            portfolio_value = (
                exchange.balance
                .available_capital
            )

            if (
                runtime_state.latest_price
                and
                "BTCUSDT"
                in exchange.positions
            ):

                position = (
                    exchange.positions[
                        "BTCUSDT"
                    ]
                )

                portfolio_value += (
                    position.quantity
                    *
                    runtime_state
                    .latest_price
                )

            session_repository.end_session(
                session_id=
                    runtime_state
                    .active_session_id,

                ended_at=
                ended_at,

                duration_seconds=
                duration_seconds,

                total_trades=
                    runtime_state
                    .total_trades,

                realized_pnl=
                    runtime_state
                    .current_unrealized_pnl,

                portfolio_value=
                    portfolio_value,

                safe_mode_triggered=
                    runtime_controller
                    .safe_mode,
            )

            print(
                f"[SESSION] "
                f"Ended session "
                f"{runtime_state.active_session_id}"
            )

        websocket.disconnect()

        runtime.shutdown()

        print(
            "[SYSTEM] "
            "Runtime stopped cleanly"
        )


if __name__ == "__main__":

    main()