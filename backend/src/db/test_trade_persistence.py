from datetime import datetime

from src.db.repository import (
    CompletedTradeRepository,
)


repository = (
    CompletedTradeRepository()
)

repository.save_completed_trade(
    symbol="BTCUSDT",

    quantity=0.01,

    entry_price=80000,

    exit_price=80500,

    realized_pnl=5.0,

    fees_paid=0.5,

    opened_at=datetime.now(),

    closed_at=datetime.now(),
)

trades = (
    repository
    .get_all_completed_trades()
)

for trade in trades:

    print(
        trade.symbol,
        trade.realized_pnl,
    )