from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from src.db.database import (
    Base,
)


class RuntimeStateEntity(Base):

    __tablename__ = "runtime_state"

    id = Column(
        Integer,
        primary_key=True,
    )

    operating_state = Column(
        String,
    )

    safe_mode = Column(
        Boolean,
    )

    total_trades = Column(
        Integer,
    )