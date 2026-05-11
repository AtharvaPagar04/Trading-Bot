from dataclasses import dataclass

from src.strategy.weighted_models import (
    WeightedStrategy,
)


@dataclass
class RoutedStrategy:

    weighted_strategy: WeightedStrategy

    allowed_regimes: list[str]