from src.runtime.runtime_monitor_loop import (
    RuntimeMonitorLoop,
)


class DummyMonitor:

    def __init__(self):

        self.tick_count = 0

    def tick(self):

        self.tick_count += 1


def test_monitor_loop_initial_state():

    monitor = DummyMonitor()

    loop = RuntimeMonitorLoop(
        monitor
    )

    assert loop.running is False


def test_monitor_loop_stop():

    monitor = DummyMonitor()

    loop = RuntimeMonitorLoop(
        monitor
    )

    loop.stop()

    assert loop.running is False