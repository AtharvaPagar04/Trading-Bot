from src.analytics.risk_of_ruin import (
    analyze_risk_of_ruin,
)

returns = [
    10,
    -20,
    15,
    -10,
    8,
]

report = (
    analyze_risk_of_ruin(
        returns=
        returns,

        simulations=1000,

        starting_capital=100,

        ruin_threshold=50,
    )
)

print(report)