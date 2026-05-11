from src.strategy.grid_anchor import (
    build_anchor_state,
)

test_cases = [
    {
        "minutes": 35,
        "adx": 18,
        "atr": 1.5,
        "emergency": False,
    },
    {
        "minutes": 20,
        "adx": 18,
        "atr": 1.5,
        "emergency": False,
    },
    {
        "minutes": 35,
        "adx": 32,
        "atr": 1.5,
        "emergency": False,
    },
    {
        "minutes": 35,
        "adx": 18,
        "atr": 4.5,
        "emergency": False,
    },
]

for case in test_cases:
    state = build_anchor_state(
        current_price=100,

        outside_range_minutes=
        case["minutes"],

        adx_value=
        case["adx"],

        atr_percent=
        case["atr"],

        emergency_active=
        case["emergency"],
    )

    print(state)