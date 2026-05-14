from collections import defaultdict
from typing import Callable
from typing import Dict
from typing import List

from src.events.base_event import BaseEvent


class EventBus:

    def __init__(self):

        self.listeners: Dict[str, List[Callable]] = defaultdict(list)
        self.global_listeners: List[Callable] = []

    def subscribe(
        self,
        event_type: str,
        callback: Callable,
    ):

        self.listeners[event_type].append(callback)

    def subscribe_all(
        self,
        callback: Callable,
    ):
        self.global_listeners.append(callback)

    def publish(
        self,
        event: BaseEvent,
    ):
        if not isinstance(
            event,
            BaseEvent,
        ):
            raise TypeError(
                "Event must inherit BaseEvent"
            )

        if event.event_type in self.listeners:
            for callback in self.listeners[event.event_type]:
                callback(event)

        for callback in self.global_listeners:
            callback(event)