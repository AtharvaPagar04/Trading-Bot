from dataclasses import dataclass


@dataclass
class StabilityExecutionDecision:

    allow_execution: bool

    confidence_multiplier: float

    reason: str