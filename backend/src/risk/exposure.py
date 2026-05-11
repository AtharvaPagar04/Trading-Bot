from dataclasses import dataclass


@dataclass
class CapitalBuckets:
    active_capital: float
    defensive_reserve: float
    emergency_reserve: float


def allocate_capital(
    total_capital: float,
) -> CapitalBuckets:
    return CapitalBuckets(
        active_capital=
        round(total_capital * 0.40, 2),

        defensive_reserve=
        round(total_capital * 0.40, 2),

        emergency_reserve=
        round(total_capital * 0.20, 2),
    )


def drawdown_size_multiplier(
    drawdown_percent: float,
) -> float:
    if drawdown_percent > 3:
        return 0.0

    if drawdown_percent > 2:
        return 0.4

    if drawdown_percent > 1:
        return 0.7

    return 1.0