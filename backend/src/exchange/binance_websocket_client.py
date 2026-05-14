import json
import threading
import time

from websocket import WebSocketApp

from src.market_data.market_data_router import (
    MarketDataRouter,
)

from src.market_data.market_tick import (
    MarketTick,
)

from datetime import datetime
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
from src.runtime.event_bus import (
    EventBus,
)


WEBSOCKET_CONNECTED_EVENT = (
    "WEBSOCKET_CONNECTED"
)


WEBSOCKET_DISCONNECTED_EVENT = (
    "WEBSOCKET_DISCONNECTED"
)
class BinanceWebSocketClient:

    def __init__(
        self,
        router: MarketDataRouter,
        event_bus: EventBus,
        symbol: str = "btcusdt",
    ):

        self.router = (
            router
        )
        self.event_bus = (
            event_bus
        )

        self.symbol = (
            symbol.lower()
        )

        self.connected = False

        self.ws = None

        self.reconnect_attempts = 0

        self.max_reconnect_attempts = 5
        self.shutdown_requested = False

        self.url = (
            f"wss://stream.binance.com:9443/ws/"
            f"{self.symbol}@trade"
        )

    def on_open(
        self,
        ws,
    ):

        self.connected = True

        self.reconnect_attempts = 0
        self.event_bus.publish(
            WEBSOCKET_CONNECTED_EVENT,
            {
                "symbol":
                self.symbol,
            },
        )

        runtime_log(
            level=LogLevel.INFO,
            category=LogCategory.WEBSOCKET,
            message=(
                f"Connected to "
                f"{self.symbol}"
            ),
        )

    def on_message(
        self,
        ws,
        message,
    ):

        try:

            data = json.loads(
                message
            )

            symbol = (
                data["s"]
            )

            price = float(
                data["p"]
            )

            tick = MarketTick(
                symbol=symbol,

                price=price,

                timestamp=
                datetime.utcnow(),

                exchange=
                "BINANCE",
            )

            self.router.route_tick(
                tick
            )

        except Exception as e:

            print(
                f"[WS ERROR] "
                f"Message parse failed: {e}"
            )

    def on_error(
        self,
        ws,
        error,
    ):

        runtime_log(
            level=LogLevel.ERROR,
            category=LogCategory.WEBSOCKET,
            message=(
                f"Websocket error: "
                f"{error}"
            ),
)

    def on_close(
        self,
        ws,
        close_status_code,
        close_msg,
    ):

        self.connected = False
        self.event_bus.publish(
            WEBSOCKET_DISCONNECTED_EVENT,
            {
                "symbol":
                self.symbol,
            },
        )

        runtime_log(
            level=LogLevel.WARNING,
            category=LogCategory.WEBSOCKET,
            message=(
                f"Websocket connection closed",
            ),
        )

        if not self.shutdown_requested:
            self.reconnect()

    def connect(
        self,
    ):
        if self.connected:

            runtime_log(
                level=LogLevel.WARNING,

                category=LogCategory.WEBSOCKET,

                message=(
                    "Connect ignored because "
                    "websocket is already connected"
                ),
            )

            return

        self.ws = WebSocketApp(
            self.url,

            on_open=
            self.on_open,

            on_message=
            self.on_message,

            on_error=
            self.on_error,

            on_close=
            self.on_close,
        )

        thread = threading.Thread(
            target=
            self.ws.run_forever
        )

        thread.daemon = True

        thread.start()

    def disconnect(
        self,
    ):
        self.shutdown_requested = True

        print(
            "[WS SHUTDOWN] "
            "Disconnect requested"
        )
        if self.ws:

            self.ws.close()

        self.connected = False

    def reconnect(
        self,
    ):

        if (
            self.reconnect_attempts
            >=
            self.max_reconnect_attempts
        ):

            print(
                "[WS FAILURE] "
                "Max reconnects exceeded"
            )

            return False

        self.reconnect_attempts += 1

        runtime_log(
            level=LogLevel.WARNING,
            category=LogCategory.WEBSOCKET,
            message=(
                f"Reconnect attempt "
                f"{self.reconnect_attempts}"
            ),
        )

        time.sleep(2)
        self.connect()

        return True