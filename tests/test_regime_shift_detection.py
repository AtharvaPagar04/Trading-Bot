from src.strategy.regime_shift_detection import (
    detect_regime_shift,
)

result = (
    detect_regime_shift(
        previous_regime=
        "RANGE",

        current_regime=
        "TREND",
    )
)

print(result)