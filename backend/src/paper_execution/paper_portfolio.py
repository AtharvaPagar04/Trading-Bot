from dataclasses import dataclass
from dataclasses import field

from src.paper_execution.paper_position import (
    PaperPosition,
)


@dataclass
class PaperPortfolio:

    cash_balance: float = 10000.0

    positions: dict[
        str,
        PaperPosition,
    ] = field(
        default_factory=dict
    )

    realized_pnl: float = 0.0
    unrealized_pnl: float = 0.0
    fees_paid: float = 0.0