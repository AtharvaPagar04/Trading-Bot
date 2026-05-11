from src.core.hierarchy_models import (
    HierarchicalIntelligenceReport,
)

from src.core.portfolio_intelligence_models import (
    PortfolioIntelligenceReport,
)

from src.portfolio.rebalance_models import (
    PortfolioRebalanceReport,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


def generate_hierarchical_intelligence(
    execution:
    StabilityExecutionDecision,

    portfolio:
    PortfolioIntelligenceReport,

    rebalance:
    PortfolioRebalanceReport,
) -> HierarchicalIntelligenceReport:

    system_confidence = (
        execution
        .confidence_multiplier
        *
        portfolio
        .final_risk_score
        *
        (
            1
            -
            rebalance
            .fragility_score
        )
    )

    return (
        HierarchicalIntelligenceReport(
            execution_layer=
            execution,

            portfolio_layer=
            portfolio,

            rebalance_layer=
            rebalance,

            system_confidence=
            system_confidence,
        )
    )