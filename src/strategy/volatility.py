from enum import Enum


class VolatilityState(str, Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    ELEVATED = "ELEVATED"
    EXTREME = "EXTREME"


def classify_volatility(
    atr_percent: float,
) -> VolatilityState:
    if atr_percent < 1:
        return VolatilityState.LOW

    if atr_percent < 3:
        return VolatilityState.NORMAL

    if atr_percent < 5:
        return VolatilityState.ELEVATED

    return VolatilityState.EXTREME