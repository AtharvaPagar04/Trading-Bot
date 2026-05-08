from dataclasses import dataclass

from src.exchange.models import (
    Balance,
    Position,
)


@dataclass
class PortfolioState:
    balance: Balance

    positions: dict[
        str,
        Position,
    ]

    cash_balance: float

    position_value: float

    total_portfolio_value: float

    unrealized_pnl: float

    total_exposure: float