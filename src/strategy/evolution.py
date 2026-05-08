from src.strategy.adaptive_weighting import (
    update_strategy_weight,
)

from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)


def evolve_strategy_weight(
    weighted_strategy: WeightedStrategy,

    attribution: StrategyAttribution,
) -> WeightedStrategy:

    weighted_strategy.realized_pnl = (
        attribution.realized_pnl
    )

    weighted_strategy.wins = (
        attribution.wins
    )

    weighted_strategy.losses = (
        attribution.losses
    )
    weighted_strategy.recent_pnls = (
        attribution.recent_pnls
    )

    weighted_strategy = (
        update_strategy_weight(
            weighted_strategy
        )
    )

    return weighted_strategy