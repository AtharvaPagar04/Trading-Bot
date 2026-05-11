from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.autonomous_decay import (
    process_regime_shift_decay,
)

from src.strategy.regime_shift_models import (
    RegimeShiftDetection,
)

attribution = (
    StrategyAttribution(
        strategy_name=
        "Momentum",

        realized_pnl=100,

        wins=10,

        losses=2,

        recent_pnls=[
            10,
            20,
            30,
        ],
    )
)

detection = (
    RegimeShiftDetection(
        regime_changed=True,

        previous_regime=
        "TREND",

        current_regime=
        "RANGE",

        trigger_reason=
        "Trend collapse",
    )
)

updated = (
    process_regime_shift_decay(
        attribution=
        attribution,

        detection=
        detection,
    )
)

print(updated)