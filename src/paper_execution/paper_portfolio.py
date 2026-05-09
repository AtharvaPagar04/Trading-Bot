from dataclasses import dataclass
from dataclasses import field


@dataclass
class PaperPortfolio:

    cash_balance: float = 10000.0

    positions: dict = field(
        default_factory=dict
    )

    average_entry_prices: dict = field(
        default_factory=dict
    )

    realized_pnl: float = 0.0