from collections import defaultdict
from collections.abc import Callable


class EventBus:

    def __init__(self):

        self.subscribers = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        handler: Callable,
    ):

        self.subscribers[
            event_type
        ].append(handler)

    def publish(
        self,
        event_type: str,
        payload,
    ):

        handlers = (
            self.subscribers.get(
                event_type,
                []
            )
        )

        for handler in handlers:

            handler(payload)