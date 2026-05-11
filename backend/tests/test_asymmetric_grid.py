from src.strategy.asymmetric_grid import (
    calculate_asymmetric_spacing,
)

base_spacings = [
    0.3,
    0.5,
    1.2,
]

for spacing in base_spacings:
    result = (
        calculate_asymmetric_spacing(
            spacing
        )
    )

    print(result)