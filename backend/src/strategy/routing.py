from src.strategy.routing_models import (
    RoutedStrategy,
)


def filter_strategies_for_regime(
    strategies:
    list[RoutedStrategy],

    regime: str,
) -> list[RoutedStrategy]:

    return [
        strategy
        for strategy
        in strategies
        if regime in (
            strategy
            .allowed_regimes
        )
    ]