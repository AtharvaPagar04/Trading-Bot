from collections import defaultdict


class RuntimeMetrics:

    def __init__(self):

        self.metrics = defaultdict(int)

    def increment(
        self,
        metric_name: str,
        value: int = 1,
    ):

        self.metrics[
            metric_name
        ] += value

    def get_metric(
        self,
        metric_name: str,
    ):

        return self.metrics.get(
            metric_name,
            0,
        )

    def report(self):

        return dict(
            self.metrics
        )