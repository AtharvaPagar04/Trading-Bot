from src.strategy.volatility import (
    classify_volatility,
)

test_values = [
    0.4,
    1.5,
    3.7,
    6.2,
]

for value in test_values:
    state = classify_volatility(value)

    print(
        f"ATR: {value}% -> "
        f"State: {state}"
    )