from statistics import mean
from statistics import pstdev

from src.analytics.performance_models import (
    AdvancedPerformanceReport,
)


def generate_advanced_performance(
    returns: list[float],
) -> AdvancedPerformanceReport:

    if len(returns) == 0:

        return (
            AdvancedPerformanceReport(
                sharpe_ratio=0,

                profit_factor=0,

                expectancy=0,

                average_return=0,

                return_volatility=0,
            )
        )

    average_return = (
        mean(returns)
    )

    volatility = 0.0

    if len(returns) > 1:

        volatility = (
            pstdev(returns)
        )

    sharpe_ratio = 0.0

    if volatility > 0:

        sharpe_ratio = (
            average_return
            / volatility
        )

    gross_profit = sum(
        r for r in returns
        if r > 0
    )

    gross_loss = abs(sum(
        r for r in returns
        if r < 0
    ))

    profit_factor = 0.0

    if gross_loss > 0:

        profit_factor = (
            gross_profit
            / gross_loss
        )

    expectancy = (
        average_return
    )

    return (
        AdvancedPerformanceReport(
            sharpe_ratio=
            sharpe_ratio,

            profit_factor=
            profit_factor,

            expectancy=
            expectancy,

            average_return=
            average_return,

            return_volatility=
            volatility,
        )
    )