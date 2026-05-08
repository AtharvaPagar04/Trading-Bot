from enum import Enum


class RegimeState(str, Enum):
    SAFE = "SAFE"
    CAUTION = "CAUTION"
    BLOCK = "BLOCK"


def classify_regime(
    adx_value: float,
) -> RegimeState:
    if adx_value < 25:
        return RegimeState.SAFE

    if adx_value <= 30:
        return RegimeState.CAUTION

    return RegimeState.BLOCK


def allow_new_entries(
    regime_state: RegimeState,
) -> bool:
    return regime_state != RegimeState.BLOCK