import time
import threading

from src.runtime.runtime_monitor import (
    RuntimeMonitor,
)

from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)
class RuntimeMonitorLoop:

    def __init__(
        self,
        monitor: RuntimeMonitor,
        interval_seconds: int = 5,
    ):

        self.monitor = monitor

        self.interval_seconds = (
            interval_seconds
        )

        self.running = False

        self.thread = None

    def run(self):

        self.running = True

        while self.running:

            try:

                self.monitor.tick()

            except Exception as exc:

                runtime_log(
                    level=LogLevel.ERROR,
                    category=LogCategory.RUNTIME,
                    message=(
                        f"Runtime monitor failure: "
                        f"{exc}"
                    ),
                )

            time.sleep(
                self.interval_seconds
            )

    def start(self):

        if self.running:
            return

        self.thread = threading.Thread(
            target=self.run,
            daemon=True,
        )

        self.thread.start()

    def stop(self):

        self.running = False