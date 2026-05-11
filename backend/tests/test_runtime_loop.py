import threading
import time

from src.runtime.event_bus import (
    EventBus,
)

from src.runtime.runtime_loop import (
    RuntimeLoop,
)


def market_handler(event):

    print(
        "EVENT RECEIVED"
    )

    print(event)


bus = EventBus()

bus.subscribe(
    "MARKET_TICK",
    market_handler,
)

runtime = RuntimeLoop(
    event_bus=bus
)

thread = threading.Thread(
    target=runtime.start
)

thread.start()

time.sleep(5)

runtime.stop()

thread.join()