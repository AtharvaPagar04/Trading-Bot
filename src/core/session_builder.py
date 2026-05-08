from datetime import datetime
from uuid import uuid4

from src.core.session import (
    TradingSession,
)


def create_trading_session(
    starting_capital: float,
) -> TradingSession:
    return TradingSession(
        session_id=str(uuid4()),

        start_time=datetime.utcnow(),

        starting_capital=
        starting_capital,

        current_capital=
        starting_capital,

        session_pnl_percent=0.0,

        peak_pnl_percent=0.0,

        entries_enabled=True,
    )