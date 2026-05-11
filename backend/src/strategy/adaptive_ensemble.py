from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.ensemble import (
    EnsembleStrategy,
)

from src.strategy.models import (
    SignalDecision,
)

from src.strategy.routing import (
    filter_strategies_for_regime,
)

from src.strategy.routing_models import (
    RoutedStrategy,
)


class AdaptiveEnsemble:

    def __init__(
        self,

        strategies:
        list[RoutedStrategy],
    ):

        self.strategies = (
            strategies
        )

    def generate_signal(
        self,

        snapshot: MarketDataSnapshot,

        regime: str,
    ) -> SignalDecision:

        filtered = (
            filter_strategies_for_regime(
                strategies=
                self.strategies,

                regime=regime,
            )
        )

        weighted_strategies = [
            strategy
            .weighted_strategy
            for strategy
            in filtered
        ]

        ensemble = (
            EnsembleStrategy(
                strategies=
                weighted_strategies
            )
        )

        return (
            ensemble
            .generate_signal(
                snapshot
            )
        )