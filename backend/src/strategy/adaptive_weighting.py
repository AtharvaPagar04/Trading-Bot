from statistics import mean

from src.strategy.weighted_models import (
    WeightedStrategy,
)


def update_strategy_weight(
    weighted_strategy: WeightedStrategy,
) -> WeightedStrategy:

    total_trades = (
        weighted_strategy.wins
        +
        weighted_strategy.losses
    )

    if total_trades == 0:

        return weighted_strategy

    win_rate = (
        weighted_strategy.wins
        / total_trades
    )

    pnl_memory = getattr(
        weighted_strategy,
        "recent_pnls",
        [],
    )

    average_recent_pnl = 0.0

    if len(pnl_memory) > 0:

        average_recent_pnl = (
            mean(pnl_memory)
        )

    pnl_factor = max(
        average_recent_pnl,
        0,
    )

    adjusted_weight = (
        (
            win_rate
            * 0.7
        )
        +
        (
            pnl_factor
            * 0.3
        )
    )

    weighted_strategy.weight = min(
        max(
            adjusted_weight,
            0.1,
        ),
        5.0,
    )

    return weighted_strategy