from src.core.integrated_runtime_models import (
    IntegratedRuntimeDecision,
)

from src.exchange.dynamic_scaling import (
    apply_confidence_scaling,
)

from src.market.market_data import (
    MarketDataSnapshot,
)

from src.strategy.adaptive_ensemble import (
    AdaptiveEnsemble,
)

from src.strategy.regime_stability import (
    analyze_regime_stability,
)

from src.strategy.stability_execution import (
    evaluate_stability_execution,
)


def execute_integrated_runtime(
    snapshot: MarketDataSnapshot,

    ensemble: AdaptiveEnsemble,

    regime: str,

    historical_regimes:
    list[str],

    base_quantity: float,
) -> IntegratedRuntimeDecision:

    stability = (
        analyze_regime_stability(
            historical_regimes
        )
    )

    execution = (
        evaluate_stability_execution(
            stability
        )
    )

    signal = (
        ensemble.generate_signal(
            snapshot=
            snapshot,

            regime=regime,
        )
    )

    scaling = (
        apply_confidence_scaling(
            quantity=
            base_quantity,

            confidence_multiplier=
            execution
            .confidence_multiplier,
        )
    )

    return (
        IntegratedRuntimeDecision(
            signal=
            signal,

            stability=
            stability,

            execution=
            execution,

            scaling=
            scaling,
        )
    )