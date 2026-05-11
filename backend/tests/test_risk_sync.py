from src.core.session_builder import (
    create_trading_session,
)

from src.core.session_update import (
    update_session_after_trade,
)

from src.risk.risk_sync import (
    synchronize_risk_state,
)

session = create_trading_session(
    starting_capital=2000
)

trade_results = [
    40,
    -50,
    -80,
    -120,
]

for pnl in trade_results:
    session = (
        update_session_after_trade(
            session=session,
            realized_pnl=pnl,
        )
    )

    risk_state = (
        synchronize_risk_state(
            session
        )
    )

    print(
        f"PnL: "
        f"{session.session_pnl_percent}% | "
        f"{risk_state}"
    )