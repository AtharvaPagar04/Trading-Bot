from src.strategy.meta_models import (
    EnsemblePerformance,
)


def select_best_ensemble(
    ensembles:
    list[EnsemblePerformance],
) -> EnsemblePerformance:

    ranked = sorted(
        ensembles,

        key=lambda ensemble:
        (
            ensemble.realized_pnl,

            ensemble.wins,
        ),

        reverse=True,
    )

    return ranked[0]