from src.exchange.models import (
    CompletedTrade,
)

from src.strategy.attribution_models import (
    StrategyAttribution,
)


MAX_MEMORY = 20


def update_strategy_attribution(
    attribution: StrategyAttribution,

    trade: CompletedTrade,
) -> StrategyAttribution:

    attribution.realized_pnl += (
        trade.realized_pnl
    )

    attribution.recent_pnls.append(
        trade.realized_pnl
    )

    if (
        len(
            attribution
            .recent_pnls
        )
        > MAX_MEMORY
    ):

        attribution.recent_pnls.pop(0)

    if trade.realized_pnl > 0:

        attribution.wins += 1

    else:

        attribution.losses += 1

    return attribution