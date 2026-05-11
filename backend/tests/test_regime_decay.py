from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.regime_decay import (
    apply_regime_memory_decay,
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
            40,
        ],
    )
)

updated = (
    apply_regime_memory_decay(
        attribution=
        attribution,

        decay_factor=0.5,
    )
)

print(updated)