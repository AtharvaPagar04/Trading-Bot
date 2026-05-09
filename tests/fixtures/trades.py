from datetime import datetime

from src.exchange.models import (
    CompletedTrade,
)


def sample_trade():

    return CompletedTrade(
        symbol="SOL/USDT",

        quantity=1,

        entry_price=100,

        exit_price=110,

        realized_pnl=10,

        fees_paid=0,

        opened_at=
        datetime.utcnow(),

        closed_at=
        datetime.utcnow(),
    )