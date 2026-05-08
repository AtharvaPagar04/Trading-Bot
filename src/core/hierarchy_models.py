from dataclasses import dataclass

from src.core.portfolio_intelligence_models import (
    PortfolioIntelligenceReport,
)

from src.portfolio.rebalance_models import (
    PortfolioRebalanceReport,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


@dataclass
class HierarchicalIntelligenceReport:

    execution_layer: (
        StabilityExecutionDecision
    )

    portfolio_layer: (
        PortfolioIntelligenceReport
    )

    rebalance_layer: (
        PortfolioRebalanceReport
    )

    system_confidence: float