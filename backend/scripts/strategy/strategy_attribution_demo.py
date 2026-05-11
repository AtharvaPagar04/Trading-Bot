from datetime import datetime

from src.exchange.models import (
    CompletedTrade,
)

from src.strategy.attribution import (
    update_strategy_attribution,
)

from src.strategy.attribution_models import (
    StrategyAttribution,
)

attribution = (
    StrategyAttribution(
        strategy_name=
        "MeanReversion",

        realized_pnl=0,

        wins=0,

        losses=0,
    )
)

trade = CompletedTrade(
    symbol="SOL/USDT",

    quantity=1,

    entry_price=100,

    exit_price=120,

    realized_pnl=20,
    fees_paid=0,

    opened_at=
    datetime.utcnow(),

    closed_at=
    datetime.utcnow(),
)

updated = (
    update_strategy_attribution(
        attribution=
        attribution,

        trade=trade,
    )
)

print(updated)