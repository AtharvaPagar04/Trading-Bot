from collections import deque
from src.monitoring.runtime_metrics import RuntimeMetrics

class MetricsHistory:
    def __init__(self, maxlen: int = 1000):
        self.buffer = deque(maxlen=maxlen)

    def record(self, metrics: RuntimeMetrics):
        self.buffer.append(metrics)

    def get_history(self) -> list[RuntimeMetrics]:
        return list(self.buffer)

metrics_history = MetricsHistory()
