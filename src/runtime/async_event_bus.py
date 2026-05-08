from collections import defaultdict
from collections.abc import Callable


class AsyncEventBus:

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

    async def publish(
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

            try:

                await handler(payload)

            except Exception as e:

                print(
                    "HANDLER ERROR"
                )

                print(e)