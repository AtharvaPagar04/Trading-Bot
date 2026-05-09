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
    ):

        self.runtime = runtime

    def route_tick(
        self,
        tick: MarketTick,
    ):

        self.runtime.market_data_heartbeat()