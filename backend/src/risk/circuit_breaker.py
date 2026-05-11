class CircuitBreaker:

    def __init__(
        self,
        failure_limit: int,
    ):

        self.failure_limit = (
            failure_limit
        )

        self.failures = 0

    def record_failure(
        self,
    ):

        self.failures += 1

    def triggered(
        self,
    ):

        return (
            self.failures
            >=
            self.failure_limit
        )
