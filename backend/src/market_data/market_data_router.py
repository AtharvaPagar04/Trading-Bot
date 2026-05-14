from src.market_data.market_tick import (
    MarketTick,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
)
from src.runtime.event_types import (
    TICK_EVENT,
)
from datetime import datetime
from src.core.events import (
    RuntimeEvent,
)

class MarketDataRouter:

    def __init__(
        self,
        runtime: GovernedRuntime,

        tick_handler=None,
    ):

        self.runtime = runtime

        self.tick_handler = (
            tick_handler
        )

    def route_tick(
        self,
        tick: MarketTick,
    ):

        event = RuntimeEvent(
            event_type=TICK_EVENT,

            payload={
                "symbol":
                tick.symbol,

                "price":
                tick.price,

                "exchange":
                tick.exchange,
            },

            emitted_at=
            datetime.utcnow(),
        )

        self.runtime.event_bus.publish(
            event
        )

        if (
            self.tick_handler
            is not None
        ):

            self.tick_handler.process_tick(
                tick
            )