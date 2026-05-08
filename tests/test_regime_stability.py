from src.strategy.regime_stability import (
    analyze_regime_stability,
)

regimes = [
    "TREND",
    "TREND",
    "TREND",
    "RANGE",
    "TREND",
    "TREND",
]

result = (
    analyze_regime_stability(
        regimes
    )
)

print(result)