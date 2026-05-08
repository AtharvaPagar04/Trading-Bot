from src.portfolio.diversification_models import (
    DiversificationReport,
)

from src.portfolio.multi_asset_models import (
    PortfolioAllocationReport,
)

from src.portfolio.rebalance_models import (
    PortfolioRebalanceReport,
)

from src.portfolio.rebalance_models import (
    RebalanceAction,
)


def rebalance_portfolio(
    allocation_report:
    PortfolioAllocationReport,

    diversification:
    DiversificationReport,
) -> PortfolioRebalanceReport:

    actions = []

    fragility = (
        diversification
        .portfolio_fragility
    )

    reduction_factor = (
        1
        -
        fragility
    )

    for allocation in (
        allocation_report
        .allocations
    ):

        new_allocation = (
            allocation
            .allocation_percent
            *
            reduction_factor
        )

        actions.append(
            RebalanceAction(
                symbol=
                allocation.symbol,

                old_allocation=
                allocation
                .allocation_percent,

                new_allocation=
                new_allocation,
            )
        )

    return (
        PortfolioRebalanceReport(
            actions=
            actions,

            fragility_score=
            fragility,
        )
    )