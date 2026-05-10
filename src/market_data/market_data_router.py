from src.market_data.market_tick import (
    MarketTick,
)

from src.runtime.governed_runtime import (
    GovernedRuntime,
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

        self.runtime.market_data_heartbeat()

        if (
            self.tick_handler
            is not None
        ):

            self.tick_handler.process_tick(
                tick
            )