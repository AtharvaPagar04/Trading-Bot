from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEvent:

    event_type: str

    emitted_at: datetime
