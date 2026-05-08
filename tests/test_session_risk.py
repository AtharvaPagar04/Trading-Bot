from src.risk.session_risk import (
    classify_session_risk,
)

test_values = [
    1.5,
    -0.5,
    -1.2,
    -2.3,
    -3.1,
    -4.5,
]

for pnl in test_values:
    state = classify_session_risk(pnl)

    print(
        f"PnL: {pnl}% -> "
        f"Risk State: {state}"
    )