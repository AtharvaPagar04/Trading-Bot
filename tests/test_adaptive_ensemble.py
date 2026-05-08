from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.strategy.adaptive_ensemble import (
    AdaptiveEnsemble,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.momentum import (
    MomentumStrategy,
)

from src.strategy.routing_models import (
    RoutedStrategy,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

snapshot = (
    load_market_snapshot_from_csv(
        filepath=
        "data/raw/sample_sol.csv",

        symbol="SOL/USDT",

        timeframe="5m",
    )
)

ensemble = (
    AdaptiveEnsemble(
        strategies=[

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
    )
)

signal = (
    ensemble.generate_signal(
        snapshot=
        snapshot,

        regime="TREND",
    )
)

print(signal)