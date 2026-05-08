from dataclasses import dataclass


@dataclass
class AdaptiveRiskBudget:

    base_risk: float

    adjusted_risk: float

    confidence_multiplier: float

    volatility_multiplier: float

    survival_multiplier: float