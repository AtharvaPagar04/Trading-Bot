from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.db.database import (
    Base,
)
from sqlalchemy import DateTime


class CandleEntity(Base):

    __tablename__ = "candles"

    id = Column(
        Integer,
        primary_key=True,
    )

    symbol = Column(
        String,
    )

    timeframe = Column(
        String,
    )

    open = Column(
        Float,
    )

    high = Column(
        Float,
    )

    low = Column(
        Float,
    )

    close = Column(
        Float,
    )

    volume = Column(
        Float,
    )

class CompletedTradeEntity(Base):

    __tablename__ = (
        "completed_trades"
    )

    id = Column(
        Integer,
        primary_key=True,
    )

    symbol = Column(
        String,
    )

    quantity = Column(
        Float,
    )

    entry_price = Column(
        Float,
    )

    exit_price = Column(
        Float,
    )

    realized_pnl = Column(
        Float,
    )

    fees_paid = Column(
        Float,
    )

    opened_at = Column(
        DateTime,
    )

    closed_at = Column(
        DateTime,
    )
    
    session_id = Column(
        Integer,
        nullable=True,
    )