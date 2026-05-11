from src.risk.profit_protection import (
    evaluate_profit_protection,
)

test_cases = [
    {
        "peak": 3.0,
        "current": 2.5,
    },
    {
        "peak": 3.0,
        "current": 2.0,
    },
    {
        "peak": 5.0,
        "current": 4.0,
    },
    {
        "peak": 5.0,
        "current": 3.0,
    },
]

for case in test_cases:
    result = evaluate_profit_protection(
        session_peak_percent=
        case["peak"],

        current_pnl_percent=
        case["current"],
    )

    print(result)