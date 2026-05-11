from src.portfolio.correlation import (
    analyze_correlations,
)

correlations = {

    ("BTC", "ETH"): 0.85,

    ("BTC", "SOL"): 0.65,

    ("ETH", "SOL"): 0.70,
}

report = (
    analyze_correlations(
        correlations
    )
)

print(report)