from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.db.database import (
    Base,
)


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