from src.strategy.attribution_models import (
    StrategyAttribution,
)


def apply_regime_memory_decay(
    attribution: StrategyAttribution,

    decay_factor: float,
) -> StrategyAttribution:

    attribution.realized_pnl *= (
        decay_factor
    )

    attribution.recent_pnls = [
        pnl * decay_factor
        for pnl
        in attribution.recent_pnls
    ]

    attribution.wins = int(
        attribution.wins
        * decay_factor
    )

    attribution.losses = int(
        attribution.losses
        * decay_factor
    )

    return attribution