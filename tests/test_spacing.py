from src.strategy.spacing import (
    calculate_dynamic_grid_spacing,
)

test_cases = [
    {
        "atr_percent": 0.20,
        "minimum_spacing": 0.30,
    },
    {
        "atr_percent": 0.45,
        "minimum_spacing": 0.30,
    },
    {
        "atr_percent": 1.20,
        "minimum_spacing": 0.30,
    },
]

for case in test_cases:
    spacing = (
        calculate_dynamic_grid_spacing(
            atr_percent=case["atr_percent"],
            minimum_spacing_percent=case[
                "minimum_spacing"
            ],
        )
    )

    print(
        f"ATR: {case['atr_percent']}% | "
        f"Minimum: {case['minimum_spacing']}% | "
        f"Final Spacing: {spacing}%"
    )