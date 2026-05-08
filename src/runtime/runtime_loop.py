import time
from datetime import datetime

from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.events import (
    MARKET_TICK,
)

from src.runtime.events import (
    RuntimeEvent,
)


class RuntimeLoop:

    def __init__(
        self,
        event_bus: EventBus,
    ):

        self.event_bus = (
            event_bus
        )

        self.running = False

    def start(self):

        self.running = True

        print(
            "Runtime loop started"
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

            self.event_bus.publish(
                event_type=
                event.event_type,

                payload=event,
            )

            time.sleep(1)

    def stop(self):

        self.running = False

        print(
            "Runtime loop stopped"
        )