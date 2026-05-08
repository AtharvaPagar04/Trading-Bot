from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.evolution import (
    evolve_strategy_weight,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

weighted_strategy = (
    WeightedStrategy(
        strategy=
        MeanReversionStrategy(),

        weight=0.5,
    )
)

attribution = (
    StrategyAttribution(
        strategy_name=
        "MeanReversion",

        realized_pnl=40,

        wins=9,

        losses=1,
    )
)

updated = (
    evolve_strategy_weight(
        weighted_strategy=
        weighted_strategy,

        attribution=
        attribution,
    )
)

print(updated)