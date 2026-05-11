from src.strategy.adaptive_weighting import (
    update_strategy_weight,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

strategy = WeightedStrategy(
    strategy=
    MeanReversionStrategy(),

    weight=0.5,

    realized_pnl=25,

    wins=8,

    losses=2,
)

updated = (
    update_strategy_weight(
        strategy
    )
)

print(updated)