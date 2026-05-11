from src.strategy.regime_stability_models import (
    RegimeStability,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


def evaluate_stability_execution(
    stability: RegimeStability,
) -> StabilityExecutionDecision:

    if (
        stability.stability_score
        < 0.4
    ):

        return (
            StabilityExecutionDecision(
                allow_execution=
                False,

                confidence_multiplier=
                0.0,

                reason=
                "Regime instability too high",
            )
        )

    if (
        stability.stability_score
        < 0.7
    ):

        return (
            StabilityExecutionDecision(
                allow_execution=
                True,

                confidence_multiplier=
                0.5,

                reason=
                "Moderate regime confidence",
            )
        )

    return (
        StabilityExecutionDecision(
            allow_execution=
            True,

            confidence_multiplier=
            1.0,

            reason=
            "Stable market structure",
        )
    )