from dataclasses import dataclass


@dataclass
class AdvancedPerformanceReport:

    sharpe_ratio: float

    profit_factor: float

    expectancy: float

    average_return: float

    return_volatility: float