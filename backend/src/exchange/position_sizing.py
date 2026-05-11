from dataclasses import dataclass

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.exchange.portfolio_risk import (
    PortfolioRiskLevel,
    PortfolioRiskState,
)


@dataclass
class PositionSizingResult:
    capital_to_deploy: float

    size_multiplier: float

    final_order_quantity: float


def calculate_position_size(
    available_capital: float,

    asset_price: float,

    runtime_state: str,

    portfolio_risk:
    PortfolioRiskState,

    volatility_percent: float,
) -> PositionSizingResult:

    base_multiplier = 1.0

    # Runtime adjustment

    if (
        runtime_state
        ==
        RuntimeOperatingState
        .REDUCE_RISK
        .value
    ):
        base_multiplier *= 0.5

    elif (
        runtime_state
        ==
        RuntimeOperatingState
        .RECOVERY
        .value
    ):
        base_multiplier *= 0.7

    elif (
        runtime_state
        ==
        RuntimeOperatingState
        .HALTED
        .value
    ):
        base_multiplier *= 0.0

    # Portfolio risk adjustment

    if (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .CAUTION
    ):
        base_multiplier *= 0.7

    elif (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .HIGH_RISK
    ):
        base_multiplier *= 0.4

    elif (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .CRITICAL
    ):
        base_multiplier *= 0.0

    # Volatility adjustment

    if volatility_percent >= 5:
        base_multiplier *= 0.4

    elif volatility_percent >= 3:
        base_multiplier *= 0.7

    # Final deployment

    capital_to_deploy = (
        available_capital
        * 0.1
        * base_multiplier
    )

    final_order_quantity = (
        capital_to_deploy
        / asset_price
    )

    return PositionSizingResult(
        capital_to_deploy=
        capital_to_deploy,

        size_multiplier=
        base_multiplier,

        final_order_quantity=
        final_order_quantity,
    )