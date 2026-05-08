from typing import Protocol

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.models import (
    SignalDecision,
)


class Strategy(
    Protocol,
):

    def generate_signal(
        self,

        snapshot: MarketDataSnapshot,
    ) -> SignalDecision:
        ...