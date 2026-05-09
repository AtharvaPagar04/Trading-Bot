import time
import threading

from src.runtime.runtime_monitor import (
    RuntimeMonitor,
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

            self.monitor.tick()

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