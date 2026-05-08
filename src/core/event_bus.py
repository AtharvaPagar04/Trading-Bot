from collections import defaultdict
from typing import Callable
from typing import Dict
from typing import List

from src.core.events import RuntimeEvent


class EventBus:

    def __init__(self):

        self.listeners: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        callback: Callable,
    ):

        self.listeners[event_type].append(callback)

    def publish(
        self,
        event: RuntimeEvent,
    ):

        if event.event_type not in self.listeners:
            return

        for callback in self.listeners[event.event_type]:
            callback(event)