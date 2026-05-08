from src.analytics.risk_of_ruin_models import (
    RiskOfRuinReport,
)

from src.core.portfolio_intelligence_models import (
    PortfolioIntelligenceReport,
)

from src.risk.risk_budget_models import (
    AdaptiveRiskBudget,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


def generate_portfolio_intelligence(
    risk_budget:
    AdaptiveRiskBudget,

    execution_decision:
    StabilityExecutionDecision,

    survivability:
    RiskOfRuinReport,
) -> PortfolioIntelligenceReport:

    final_risk_score = (
        risk_budget
        .adjusted_risk
        *
        execution_decision
        .confidence_multiplier
        *
        survivability
        .survival_rate
    )

    return (
        PortfolioIntelligenceReport(
            risk_budget=
            risk_budget,

            execution_decision=
            execution_decision,

            survivability=
            survivability,

            final_risk_score=
            final_risk_score,
        )
    )