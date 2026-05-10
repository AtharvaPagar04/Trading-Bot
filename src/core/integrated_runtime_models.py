from dataclasses import dataclass

from src.exchange.dynamic_scaling_models import (
    DynamicPositionSizing,
)

from src.strategy.models import (
    SignalDecision,
)

from src.strategy.regime_stability_models import (
    RegimeStability,
)

from src.strategy.stability_execution_models import (
    StabilityExecutionDecision,
)


@dataclass
class IntegratedRuntimeDecision:

    signal: SignalDecision

    stability: RegimeStability

    execution: StabilityExecutionDecision

    scaling: DynamicPositionSizing


@dataclass
class MarketDataSnapshot:

    symbol: str

    price: float

    timestamp: object