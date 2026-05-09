from src.backtest.analytics import (
    generate_performance_report,
)

from src.exchange.models import (
    CompletedTrade,
)

from datetime import datetime

trades = [

    CompletedTrade(
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
    ),

    CompletedTrade(
        symbol="SOL/USDT",

        quantity=1,

        entry_price=100,

        exit_price=95,

        realized_pnl=-5,

        opened_at=
        datetime.utcnow(),

        closed_at=
        datetime.utcnow(),
    ),

    CompletedTrade(
        symbol="SOL/USDT",

        quantity=1,

        entry_price=100,

        exit_price=120,

        realized_pnl=20,

        opened_at=
        datetime.utcnow(),

        closed_at=
        datetime.utcnow(),
    ),
]

report = (
    generate_performance_report(
        trades
    )
)

print(report)