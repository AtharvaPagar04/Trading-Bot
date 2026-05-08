from src.strategy.regime_stability_models import (
    RegimeStability,
)

from src.strategy.stability_execution import (
    evaluate_stability_execution,
)

stability = (
    RegimeStability(
        dominant_regime=
        "TREND",

        stability_score=0.55,

        transitions=4,

        total_samples=10,
    )
)

decision = (
    evaluate_stability_execution(
        stability
    )
)

print(decision)