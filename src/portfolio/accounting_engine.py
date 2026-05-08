from src.portfolio.accounting_models import (
    PortfolioPosition,
)

from src.portfolio.accounting_models import (
    PortfolioSnapshot,
)


class PortfolioAccountingEngine:

    def __init__(
        self,
        initial_cash: float = 10000,
    ):

        self.cash_balance = (
            initial_cash
        )

        self.realized_pnl = 0

        self.positions = {}

    def open_position(
        self,
        symbol: str,
        quantity: float,
        entry_price: float,
    ):

        cost = (
            quantity
            *
            entry_price
        )

        self.cash_balance -= cost

        self.positions[
            symbol
        ] = PortfolioPosition(
            symbol=symbol,

            quantity=quantity,

            average_entry_price=
            entry_price,

            market_price=
            entry_price,

            unrealized_pnl=0,
        )

    def update_market_price(
        self,
        symbol: str,
        market_price: float,
    ):

        position = (
            self.positions.get(
                symbol
            )
        )

        if position is None:

            return

        position.market_price = (
            market_price
        )

        position.unrealized_pnl = (
            (
                market_price
                -
                position.average_entry_price
            )
            *
            position.quantity
        )

    def close_position(
        self,
        symbol: str,
    ):

        position = (
            self.positions.get(
                symbol
            )
        )

        if position is None:

            return

        realized = (
            (
                position.market_price
                -
                position.average_entry_price
            )
            *
            position.quantity
        )

        self.realized_pnl += (
            realized
        )

        self.cash_balance += (
            position.quantity
            *
            position.market_price
        )

        del self.positions[
            symbol
        ]

    def portfolio_snapshot(self):

        unrealized = sum(
            (
                p.unrealized_pnl
            )
            for p in (
                self.positions
                .values()
            )
        )

        exposure = sum(
            (
                p.quantity
                *
                p.market_price
            )
            for p in (
                self.positions
                .values()
            )
        )

        equity = (
            self.cash_balance
            +
            exposure
        )

        return PortfolioSnapshot(
            cash_balance=
            self.cash_balance,

            total_equity=
            equity,

            realized_pnl=
            self.realized_pnl,

            unrealized_pnl=
            unrealized,

            exposure=
            exposure,

            positions=list(
                self.positions
                .values()
            ),
        )