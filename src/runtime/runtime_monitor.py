from src.runtime.governed_runtime import (
    GovernedRuntime,
)


class RuntimeMonitor:

    def __init__(
        self,
        runtime: GovernedRuntime,
    ):

        self.runtime = runtime

    def tick(self):

        self.runtime.validate_heartbeat()