from src.strategy.ensemble_selection import (
    select_best_ensemble,
)

from src.strategy.meta_models import (
    EnsemblePerformance,
)

trend = (
    EnsemblePerformance(
        ensemble_name=
        "TREND_ENSEMBLE",

        realized_pnl=50,

        wins=8,

        losses=2,

        usage_count=10,
    )
)

range_system = (
    EnsemblePerformance(
        ensemble_name=
        "RANGE_ENSEMBLE",

        realized_pnl=20,

        wins=5,

        losses=5,

        usage_count=10,
    )
)

selected = (
    select_best_ensemble(
        [
            trend,
            range_system,
        ]
    )
)

print(selected)