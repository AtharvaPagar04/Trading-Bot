import asyncio
import json

import websockets

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.runtime.events import (
    MARKET_TICK,
)

from src.runtime.events import (
    RuntimeEvent,
)

from datetime import datetime


class BinanceWebsocketClient:

    def __init__(
        self,
        event_bus: AsyncEventBus,
        symbol: str = "btcusdt",
    ):

        self.event_bus = (
            event_bus
        )

        self.symbol = symbol

        self.running = False

    async def connect(self):

        self.running = True

        url = (
            f"wss://stream.binance.com:9443/ws/"
            f"{self.symbol}@trade"
        )

        print(
            f"Connecting to {url}"
        )

        async with websockets.connect(
            url
        ) as websocket:

            print(
                "Connected to Binance"
            )

            while self.running:

                raw_message = (
                    await websocket.recv()
                )

                data = json.loads(
                    raw_message
                )

                event = RuntimeEvent(
                    event_type=
                    MARKET_TICK,

                    payload={
                        "symbol":
                        data["s"],

                        "price":
                        float(
                            data["p"]
                        ),

                        "quantity":
                        float(
                            data["q"]
                        ),
                    },

                    timestamp=
                    datetime.utcnow(),
                )

                await self.event_bus.publish(
                    event_type=
                    MARKET_TICK,

                    payload=
                    event,
                )

    def stop(self):

        self.running = False

        print(
            "Binance websocket stopped"
        )