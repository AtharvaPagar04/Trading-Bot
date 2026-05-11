from dataclasses import dataclass

from src.core.state import (
    RegimeState,
)


@dataclass
class RegimeResult:
    regime_state: RegimeState

    allow_entries: bool


def evaluate_market_regime(
    adx_value: float,
) -> RegimeResult:

    if adx_value >= 35:
        return RegimeResult(
            regime_state=
            RegimeState.BLOCK,

            allow_entries=False,
        )

    if adx_value >= 25:
        return RegimeResult(
            regime_state=
            RegimeState.CAUTION,

            allow_entries=True,
        )

    return RegimeResult(
        regime_state=
        RegimeState.SAFE,

        allow_entries=True,
    )