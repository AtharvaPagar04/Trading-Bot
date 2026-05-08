from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.momentum import (
    MomentumStrategy,
)

from src.strategy.routing import (
    filter_strategies_for_regime,
)

from src.strategy.routing_models import (
    RoutedStrategy,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

strategies = [

    RoutedStrategy(
        weighted_strategy=
        WeightedStrategy(
            strategy=
            MeanReversionStrategy(),

            weight=0.4,
        ),

        allowed_regimes=[
            "RANGE",
            "SAFE",
        ],
    ),

    RoutedStrategy(
        weighted_strategy=
        WeightedStrategy(
            strategy=
            MomentumStrategy(),

            weight=0.6,
        ),

        allowed_regimes=[
            "TREND",
            "BREAKOUT",
        ],
    ),
]

filtered = (
    filter_strategies_for_regime(
        strategies=
        strategies,

        regime="TREND",
    )
)

print(filtered)