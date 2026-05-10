import time

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


def main():

    event_bus = EventBus()

    runtime = GovernedRuntime(
        RuntimeMode.DRY_RUN,
        event_bus,
    )

    runtime.start()

    runtime_state = (
        build_runtime_state(
            capital=2000,

            timeframe="5m",

            adx_value=20,

            atr_percent=1.5,
        )
    )

    exchange = (
        PaperExchange(
            starting_capital=2000
        )
    )

    tick_handler = (
        LiveTickHandler(
            runtime_state=
            runtime_state,

            exchange=
            exchange,
        )
    )

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

    websocket.connect()

    print(
        "[SYSTEM] "
        "Live paper trading "
        "runtime started"
    )

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        print(
            "\n[SYSTEM] "
            "Shutdown requested"
        )

        websocket.disconnect()

        runtime.shutdown()

        print(
            "[SYSTEM] "
            "Runtime stopped cleanly"
        )


if __name__ == "__main__":

    main()