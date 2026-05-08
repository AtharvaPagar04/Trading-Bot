from dataclasses import dataclass


@dataclass
class DiversificationReport:

    diversification_score: float

    concentration_risk: float

    average_correlation: float

    portfolio_fragility: float