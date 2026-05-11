from src.analytics.performance import (
    generate_advanced_performance,
)

returns = [
    10,
    -5,
    8,
    12,
    -3,
]

report = (
    generate_advanced_performance(
        returns
    )
)

print(report)