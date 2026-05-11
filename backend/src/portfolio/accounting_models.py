from dataclasses import dataclass


@dataclass
class PortfolioPosition:

    symbol: str

    quantity: float

    average_entry_price: float

    market_price: float

    unrealized_pnl: float


@dataclass
class PortfolioSnapshot:

    cash_balance: float

    total_equity: float

    realized_pnl: float

    unrealized_pnl: float

    exposure: float

    positions: list