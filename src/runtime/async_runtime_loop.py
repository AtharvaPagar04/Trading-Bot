import asyncio
from datetime import datetime

from src.runtime.async_event_bus import (
    AsyncEventBus,
)

from src.core.events import (
    MARKET_TICK,
    RuntimeEvent,
)


class AsyncRuntimeLoop:

    def __init__(
        self,
        event_bus: AsyncEventBus,
    ):

        self.event_bus = (
            event_bus
        )

        self.running = False

    async def start(self):

        self.running = True

        print(
            "Async runtime started"
        )

        while self.running:

            event = RuntimeEvent(
                event_type=
                MARKET_TICK,

                payload={
                    "symbol":
                    "BTC/USDT",

                    "price":
                    100000,
                },

                timestamp=
                datetime.utcnow(),
            )

            await self.event_bus.publish(
                event_type=
                event.event_type,

                payload=
                event,
            )

            await asyncio.sleep(1)

    def stop(self):

        self.running = False

        print(
            "Async runtime stopped"
        )