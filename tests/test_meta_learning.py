from src.strategy.meta_learning import (
    update_ensemble_performance,
)

from src.strategy.meta_models import (
    EnsemblePerformance,
)

performance = (
    EnsemblePerformance(
        ensemble_name=
        "TREND_ENSEMBLE",

        realized_pnl=0,

        wins=0,

        losses=0,

        usage_count=0,
    )
)

updated = (
    update_ensemble_performance(
        performance=
        performance,

        realized_pnl=25,
    )
)

print(updated)