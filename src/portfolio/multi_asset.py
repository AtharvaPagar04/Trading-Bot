from src.portfolio.multi_asset_models import (
    AssetAllocation,
)

from src.portfolio.multi_asset_models import (
    PortfolioAllocationReport,
)


def generate_portfolio_allocations(
    confidence_scores:
    dict[str, float],
) -> PortfolioAllocationReport:

    total_confidence = sum(
        confidence_scores.values()
    )

    allocations = []

    for (
        symbol,
        confidence
    ) in confidence_scores.items():

        allocation = 0.0

        if total_confidence > 0:

            allocation = (
                confidence
                / total_confidence
            )

        allocations.append(
            AssetAllocation(
                symbol=symbol,

                allocation_percent=
                allocation,

                confidence_score=
                confidence,
            )
        )

    total_allocated = sum(
        allocation
        .allocation_percent

        for allocation
        in allocations
    )

    return (
        PortfolioAllocationReport(
            allocations=
            allocations,

            total_allocated=
            total_allocated,
        )
    )