from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from src.db.database import (
    Base,
)



class TradeExecutionEntity(Base):

    __tablename__ = "executions"

    id = Column(
        Integer,
        primary_key=True,
    )

    symbol = Column(
        String,
    )

    side = Column(
        String,
    )

    quantity = Column(
        Float,
    )

    price = Column(
        Float,
    )

    realized_pnl = Column(
        Float,
    )