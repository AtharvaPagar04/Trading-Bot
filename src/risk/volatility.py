from src.core.state import (
    VolatilityState,
)


def classify_volatility(
    atr_percent: float,
) -> VolatilityState:

    if atr_percent >= 5:
        return (
            VolatilityState
            .EXTREME
        )

    if atr_percent >= 3:
        return (
            VolatilityState
            .ELEVATED
        )

    if atr_percent >= 1:
        return (
            VolatilityState
            .NORMAL
        )

    return (
        VolatilityState
        .LOW
    )