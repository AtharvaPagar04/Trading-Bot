from src.market.csv_provider import (
    load_market_snapshot_from_csv,
)

from src.strategy.ensemble import (
    EnsembleStrategy,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.momentum import (
    MomentumStrategy,
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



ensemble = EnsembleStrategy(
    strategies=[

        WeightedStrategy(
            strategy=
            MeanReversionStrategy(),

            weight=0.4,
        ),

        WeightedStrategy(
            strategy=
            MomentumStrategy(),

            weight=0.6,
        ),
    ]
)

signal = (
    ensemble.generate_signal(
        snapshot
    )
)

print(signal)