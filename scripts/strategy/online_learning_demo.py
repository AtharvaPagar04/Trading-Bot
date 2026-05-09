from datetime import datetime

from src.exchange.models import (
    CompletedTrade,
)

from src.strategy.attribution_models import (
    StrategyAttribution,
)

from src.strategy.mean_reversion import (
    MeanReversionStrategy,
)

from src.strategy.online_learning import (
    process_completed_trade,
)

from src.strategy.weighted_models import (
    WeightedStrategy,
)

strategy = (
    WeightedStrategy(
        strategy=
        MeanReversionStrategy(),

        weight=0.5,
    )
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

    exit_price=130,

    realized_pnl=30,

    fees_paid=0,

    opened_at=
    datetime.utcnow(),

    closed_at=
    datetime.utcnow(),
)

updated = (
    process_completed_trade(
        weighted_strategy=
        strategy,

        attribution=
        attribution,

        trade=trade,
    )
)

print(updated)