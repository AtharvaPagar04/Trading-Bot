from dataclasses import dataclass


@dataclass
class RecoveryState:
    adx_safe: bool
    atr_safe: bool
    candles_stable: bool

    reentry_allowed: bool


def validate_reentry_conditions(
    adx_value: float,
    atr_percent: float,
    stable_candle_closes: int,
) -> RecoveryState:
    adx_safe = adx_value < 25

    atr_safe = atr_percent < 3

    candles_stable = (
        stable_candle_closes >= 2
    )

    reentry_allowed = all(
        [
            adx_safe,
            atr_safe,
            candles_stable,
        ]
    )

    return RecoveryState(
        adx_safe=adx_safe,
        atr_safe=atr_safe,
        candles_stable=
        candles_stable,

        reentry_allowed=
        reentry_allowed,
    )
    