from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.regime_decay import (
    apply_regime_memory_decay,
)

from src.strategy.regime_shift_models import (
    RegimeShiftDetection,
)


def process_regime_shift_decay(
    attribution: StrategyAttribution,

    detection: RegimeShiftDetection,
) -> StrategyAttribution:

    if (
        detection.regime_changed
    ):

        attribution = (
            apply_regime_memory_decay(
                attribution=
                attribution,

                decay_factor=0.5,
            )
        )

    return attribution