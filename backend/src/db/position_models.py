from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.db.database import (
    Base,
)


class PositionEntity(Base):

    __tablename__ = "positions"

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

    average_price = Column(
        Float,
    )

    current_price = Column(
        Float,
    )

    unrealized_pnl = Column(
        Float,
    )

    status = Column(
        String,
    )