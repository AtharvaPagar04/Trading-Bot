from src.core.session_builder import (
    create_trading_session,
)

from src.core.session_update import (
    update_session_after_trade,
)

session = create_trading_session(
    starting_capital=2000
)

trade_results = [
    50,
    -20,
    40,
    -100,
]

for pnl in trade_results:
    session = (
        update_session_after_trade(
            session=session,
            realized_pnl=pnl,
        )
    )

    print(session)