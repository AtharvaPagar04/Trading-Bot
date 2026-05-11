from dataclasses import dataclass
from enum import Enum

from src.exchange.portfolio import (
    PortfolioState,
)


class PortfolioRiskLevel(
    str,
    Enum,
):
    NORMAL = "NORMAL"

    CAUTION = "CAUTION"

    HIGH_RISK = (
        "HIGH_RISK"
    )

    CRITICAL = (
        "CRITICAL"
    )


@dataclass
class PortfolioRiskState:
    risk_level: PortfolioRiskLevel

    utilization_percent: float

    exposure_percent: float

    pnl_percent: float

    allow_new_entries: bool


def evaluate_portfolio_risk(
    portfolio: PortfolioState,
) -> PortfolioRiskState:

    total_capital = (
        portfolio.balance
        .total_capital
    )

    exposure_percent = (
        (
            portfolio.total_exposure
            / total_capital
        )
        * 100
    )

    utilization_percent = (
        (
            (
                total_capital
                -
                portfolio.balance
                .available_capital
            )
            / total_capital
        )
        * 100
    )

    pnl_percent = (
        (
            portfolio.unrealized_pnl
            / total_capital
        )
        * 100
    )
    
    if exposure_percent >= 95:

        return PortfolioRiskState(
            risk_level=
            PortfolioRiskLevel
            .CRITICAL,

            utilization_percent=
            utilization_percent,

            exposure_percent=
            exposure_percent,

            pnl_percent=
            pnl_percent,

            allow_new_entries=
            False,
        )
    if pnl_percent <= -15:

        return PortfolioRiskState(
            risk_level=
            PortfolioRiskLevel
            .CRITICAL,

            utilization_percent=
            utilization_percent,

            exposure_percent=
            exposure_percent,

            pnl_percent=
            pnl_percent,

            allow_new_entries=
            False,
        )

    if pnl_percent <= -8:

        return PortfolioRiskState(
            risk_level=
            PortfolioRiskLevel
            .HIGH_RISK,

            utilization_percent=
            utilization_percent,

            exposure_percent=
            exposure_percent,

            pnl_percent=
            pnl_percent,

            allow_new_entries=
            False,
        )

    if pnl_percent <= -3:

        return PortfolioRiskState(
            risk_level=
            PortfolioRiskLevel
            .CAUTION,

            utilization_percent=
            utilization_percent,

            exposure_percent=
            exposure_percent,

            pnl_percent=
            pnl_percent,

            allow_new_entries=
            True,
        )

    return PortfolioRiskState(
        risk_level=
        PortfolioRiskLevel
        .NORMAL,

        utilization_percent=
        utilization_percent,

        exposure_percent=
        exposure_percent,

        pnl_percent=
        pnl_percent,

        allow_new_entries=
        True,
    )