from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer

from src.db.database import (
    Base,
)


class BalanceEntity(Base):

    __tablename__ = "balance"

    id = Column(
        Integer,
        primary_key=True,
    )

    total_capital = Column(
        Float,
    )

    available_capital = Column(
        Float,
    )