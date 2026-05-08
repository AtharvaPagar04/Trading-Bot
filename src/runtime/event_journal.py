import json
from datetime import datetime

from src.db.database import (
    SessionLocal,
)

from src.db.event_models import (
    RuntimeEventEntity,
)


class EventJournal:

    def __init__(self):

        self.session = (
            SessionLocal()
        )

    def log_event(
        self,
        event_type: str,
        payload: dict,
    ):

        event = (
            RuntimeEventEntity(
                event_type=
                event_type,

                event_payload=
                json.dumps(
                    payload
                ),

                event_timestamp=
                str(
                    datetime.utcnow()
                ),
            )
        )

        self.session.add(
            event
        )

        self.session.commit()

    def get_events(self):

        return (
            self.session.query(
                RuntimeEventEntity
            ).all()
        )