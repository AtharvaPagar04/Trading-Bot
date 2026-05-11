from src.strategy.meta_models import (
    EnsemblePerformance,
)


def update_ensemble_performance(
    performance: EnsemblePerformance,

    realized_pnl: float,
) -> EnsemblePerformance:

    performance.realized_pnl += (
        realized_pnl
    )

    performance.usage_count += 1

    if realized_pnl > 0:

        performance.wins += 1

    else:

        performance.losses += 1

    return performance