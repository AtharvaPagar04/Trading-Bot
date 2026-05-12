from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
)

from src.db.database import (
    Base,
)

class TradingSessionModel(
    Base,
):

    __tablename__ = (
        "trading_sessions"
    )

    id = Column(
        Integer,
        primary_key=True,
    )

    started_at = Column(
        DateTime,
        nullable=False,
    )

    ended_at = Column(
        DateTime,
        nullable=True,
    )

    duration_seconds = Column(
        Integer,
        default=0,
    )

    total_trades = Column(
        Integer,
        default=0,
    )

    realized_pnl = Column(
        Float,
        default=0.0,
    )

    portfolio_value = Column(
        Float,
        default=0.0,
    )

    safe_mode_triggered = Column(
        Boolean,
        default=False,
    )