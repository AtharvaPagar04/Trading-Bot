from src.strategy.attribution import (
    update_strategy_attribution,
)

from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.evolution import (
    evolve_strategy_weight,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

from src.exchange.models import (
    CompletedTrade,
)


def process_completed_trade(
    weighted_strategy: WeightedStrategy,

    attribution: StrategyAttribution,

    trade: CompletedTrade,
) -> WeightedStrategy:

    attribution = (
        update_strategy_attribution(
            attribution=
            attribution,

            trade=trade,
        )
    )

    weighted_strategy = (
        evolve_strategy_weight(
            weighted_strategy=
            weighted_strategy,

            attribution=
            attribution,
        )
    )

    return weighted_strategy