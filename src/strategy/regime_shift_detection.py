from src.strategy.regime_shift_models import (
    RegimeShiftDetection,
)


def detect_regime_shift(
    previous_regime: str,

    current_regime: str,
) -> RegimeShiftDetection:

    changed = (
        previous_regime
        !=
        current_regime
    )

    reason = (
        "No regime shift"
    )

    if changed:

        reason = (
            f"Regime changed from "
            f"{previous_regime} "
            f"to "
            f"{current_regime}"
        )

    return RegimeShiftDetection(
        regime_changed=
        changed,

        previous_regime=
        previous_regime,

        current_regime=
        current_regime,

        trigger_reason=
        reason,
    )