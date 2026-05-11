from src.analytics.risk_of_ruin_models import (
    RiskOfRuinReport,
)

from src.core.portfolio_intelligence import (
    generate_portfolio_intelligence,
)

from src.risk.risk_budget_models import (
    AdaptiveRiskBudget,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)

risk_budget = (
    AdaptiveRiskBudget(
        base_risk=0.02,

        adjusted_risk=0.01,

        confidence_multiplier=0.8,

        volatility_multiplier=0.7,

        survival_multiplier=0.9,
    )
)

execution = (
    StabilityExecutionDecision(
        allow_execution=True,

        confidence_multiplier=0.8,

        reason=
        "Stable environment",
    )
)

survivability = (
    RiskOfRuinReport(
        simulations=1000,

        ruin_count=0,

        survival_rate=1.0,

        ruin_probability=0.0,
    )
)

report = (
    generate_portfolio_intelligence(
        risk_budget=
        risk_budget,

        execution_decision=
        execution,

        survivability=
        survivability,
    )
)

print(report)