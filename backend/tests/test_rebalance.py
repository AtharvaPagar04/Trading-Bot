from src.portfolio.correlation import (
    analyze_correlations,
)

from src.portfolio.diversification import (
    evaluate_diversification,
)

from src.portfolio.multi_asset import (
    generate_portfolio_allocations,
)

from src.portfolio.rebalance import (
    rebalance_portfolio,
)

scores = {
    "BTC": 0.9,
    "ETH": 0.6,
    "SOL": 0.5,
}

allocations = (
    generate_portfolio_allocations(
        scores
    )
)

correlations = {

    ("BTC", "ETH"): 0.85,

    ("BTC", "SOL"): 0.65,

    ("ETH", "SOL"): 0.70,
}

correlation_report = (
    analyze_correlations(
        correlations
    )
)

diversification = (
    evaluate_diversification(
        correlation_report
    )
)

report = (
    rebalance_portfolio(
        allocation_report=
        allocations,

        diversification=
        diversification,
    )
)

print(report)