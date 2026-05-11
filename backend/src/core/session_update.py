from src.core.session import (
    TradingSession,
)


def update_session_after_trade(
    session: TradingSession,
    realized_pnl: float,
) -> TradingSession:
    new_capital = (
        session.current_capital
        + realized_pnl
    )

    pnl_percent = (
        (
            new_capital
            - session.starting_capital
        )
        / session.starting_capital
    ) * 100

    peak_pnl = max(
        session.peak_pnl_percent,
        pnl_percent,
    )

    session.current_capital = round(
        new_capital,
        2,
    )

    session.session_pnl_percent = round(
        pnl_percent,
        4,
    )

    session.peak_pnl_percent = round(
        peak_pnl,
        4,
    )

    return session