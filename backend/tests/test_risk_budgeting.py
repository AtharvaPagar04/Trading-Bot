from src.risk.risk_budgeting import (
    calculate_adaptive_risk_budget,
)

result = (
    calculate_adaptive_risk_budget(
        base_risk=0.02,

        confidence_multiplier=0.8,

        volatility_multiplier=0.7,

        survival_multiplier=0.9,
    )
)

print(result)