from src.risk.recovery import (
    validate_reentry_conditions,
)

test_cases = [
    {
        "adx": 18,
        "atr": 1.5,
        "stable_closes": 2,
    },
    {
        "adx": 28,
        "atr": 1.5,
        "stable_closes": 2,
    },
    {
        "adx": 18,
        "atr": 4.2,
        "stable_closes": 2,
    },
    {
        "adx": 18,
        "atr": 1.5,
        "stable_closes": 1,
    },
]

for case in test_cases:
    result = validate_reentry_conditions(
        adx_value=case["adx"],
        atr_percent=case["atr"],
        stable_candle_closes=
        case["stable_closes"],
    )

    print(result)