from dataclasses import dataclass


@dataclass
class SimulatedExecution:

    requested_price: float

    executed_price: float

    quantity_requested: float

    quantity_filled: float

    slippage: float

    latency_ms: int

    execution_successful: bool

    rejection_reason: str | None