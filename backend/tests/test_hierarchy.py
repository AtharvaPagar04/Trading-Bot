from src.analytics.risk_of_ruin_models import (
    RiskOfRuinReport,
)

from src.core.hierarchy import (
    generate_hierarchical_intelligence,
)

from src.core.portfolio_intelligence import (
    generate_portfolio_intelligence,
)

from src.portfolio.rebalance_models import (
    PortfolioRebalanceReport,
)

from src.portfolio.rebalance_models import (
    RebalanceAction,
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
        "Stable market",
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

portfolio = (
    generate_portfolio_intelligence(
        risk_budget=
        risk_budget,

        execution_decision=
        execution,

        survivability=
        survivability,
    )
)

rebalance = (
    PortfolioRebalanceReport(
        actions=[
            RebalanceAction(
                symbol="BTC",

                old_allocation=0.45,

                new_allocation=0.20,
            )
        ],

        fragility_score=0.5,
    )
)

report = (
    generate_hierarchical_intelligence(
        execution=
        execution,

        portfolio=
        portfolio,

        rebalance=
        rebalance,
    )
)

print(report)