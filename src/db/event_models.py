from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from src.db.database import (
    Base,
)


class RuntimeEventEntity(Base):

    __tablename__ = "runtime_events"

    id = Column(
        Integer,
        primary_key=True,
    )

    event_type = Column(
        String,
    )

    event_payload = Column(
        Text,
    )

    event_timestamp = Column(
        String,
    )