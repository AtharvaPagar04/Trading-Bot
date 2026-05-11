class MetricsRegistry:

    def __init__(
        self,
    ):

        self.metrics = {}

    def increment(
        self,
        key: str,
    ):

        current = (
            self.metrics.get(
                key,
                0,
            )
        )

        self.metrics[key] = (
            current
            +
            1
        )

    def get_metric(
        self,
        key: str,
    ):

        return (
            self.metrics.get(
                key,
                0,
            )
        )
