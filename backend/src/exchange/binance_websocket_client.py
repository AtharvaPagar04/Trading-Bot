import json
import threading

from websocket import WebSocketApp

from src.market_data.market_data_router import (
    MarketDataRouter,
)

from src.market_data.market_tick import (
    MarketTick,
)

from datetime import datetime


class BinanceWebSocketClient:

    def __init__(
        self,
        router: MarketDataRouter,
        symbol: str = "btcusdt",
    ):

        self.router = router

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

        print(
            f"[WS OPEN] Connected to "
            f"{self.symbol}"
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

        print(
            f"[WS ERROR] {error}"
        )

    def on_close(
        self,
        ws,
        close_status_code,
        close_msg,
    ):

        self.connected = False

        print(
            "[WS CLOSED]"
        )
        if not self.shutdown_requested:
            self.reconnect()

    def connect(
        self,
    ):

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

        print(
            f"[WS RECONNECT] "
            f"Attempt "
            f"{self.reconnect_attempts}"
        )

        self.connect()

        return True