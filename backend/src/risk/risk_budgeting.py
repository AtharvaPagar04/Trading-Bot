from src.risk.risk_budget_models import (
    AdaptiveRiskBudget,
)


def calculate_adaptive_risk_budget(
    base_risk: float,

    confidence_multiplier: float,

    volatility_multiplier: float,

    survival_multiplier: float,
) -> AdaptiveRiskBudget:

    adjusted_risk = (
        base_risk
        *
        confidence_multiplier
        *
        volatility_multiplier
        *
        survival_multiplier
    )

    return AdaptiveRiskBudget(
        base_risk=
        base_risk,

        adjusted_risk=
        adjusted_risk,

        confidence_multiplier=
        confidence_multiplier,

        volatility_multiplier=
        volatility_multiplier,

        survival_multiplier=
        survival_multiplier,
    )