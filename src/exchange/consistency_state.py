from dataclasses import (
    dataclass,
)


@dataclass
class ConsistencyState:

    drift_detected: bool = False

    last_reconciliation_successful: bool = True
