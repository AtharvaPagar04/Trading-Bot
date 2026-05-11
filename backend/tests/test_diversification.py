from src.portfolio.correlation import (
    analyze_correlations,
)

from src.portfolio.diversification import (
    evaluate_diversification,
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

report = (
    evaluate_diversification(
        correlation_report
    )
)

print(report)