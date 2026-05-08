from dataclasses import dataclass

from src.analytics.risk_of_ruin_models import (
    RiskOfRuinReport,
)

from src.risk.risk_budget_models import (
    AdaptiveRiskBudget,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


@dataclass
class PortfolioIntelligenceReport:

    risk_budget: AdaptiveRiskBudget

    execution_decision: (
        StabilityExecutionDecision
    )

    survivability: (
        RiskOfRuinReport
    )

    final_risk_score: float