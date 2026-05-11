from src.core.session_builder import (
    create_trading_session,
)

from src.core.session_update import (
    update_session_after_trade,
)

from src.risk.risk_sync import (
    synchronize_risk_state,
)

from src.risk.risk_events import (
    generate_risk_events,
)

session = create_trading_session(
    starting_capital=2000
)

trade_results = [
    -20,
    -50,
    -80,
    -120,
]
previous_risk_state = None
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

    events = generate_risk_events(
        previous_state=
        previous_risk_state,

        current_state=
        risk_state,
    )

    print(
        f"\nPnL: "
        f"{session.session_pnl_percent}%"
    )
    

    for event in events:
        print(event)
    previous_risk_state = (
        risk_state.risk_state
    )   