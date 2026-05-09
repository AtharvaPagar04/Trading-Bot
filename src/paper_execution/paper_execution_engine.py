from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)
from src.paper_execution.paper_position import (
    PaperPosition,
)

class PaperExecutionEngine:

    def __init__(
        self,
        runtime: GovernedRuntime,
    ):

        self.runtime = runtime

        self.executed_orders = []

        self.portfolio = (
            PaperPortfolio()
        )

    def execute_order(
        self,
        order: PaperOrder,
    ) -> bool:

        if not (
            self.runtime
            .execution_allowed()
        ):
            return False

        notional = (
            order.quantity
            *
            order.price
        )

        if order.side == "BUY":

            if (
                self.portfolio.cash_balance
                < notional
            ):
                return False

            self.portfolio.cash_balance -= (
                notional
            )

            position = (
                self.portfolio.positions
                .get(order.symbol)
            )

            if position is None:

                position = PaperPosition(
                    symbol=order.symbol,
                )

                self.portfolio.positions[
                    order.symbol
                ] = position

            position = (
                self.portfolio.positions
                .get(order.symbol)
            )

            if position is None:

                position = PaperPosition(
                    symbol=order.symbol,
                )

                self.portfolio.positions[
                    order.symbol
                ] = position

            existing_quantity = (
                position.quantity
            )

            existing_notional = (
                existing_quantity
                *
                position.average_entry_price
            )

            new_notional = (
                order.quantity
                *
                order.price
            )

            new_total_quantity = (
                existing_quantity
                +
                order.quantity
            )

            position.average_entry_price = (
                (
                    existing_notional
                    +
                    new_notional
                )
                /
                new_total_quantity
            )

            position.quantity = (
                new_total_quantity
            )

        elif order.side == "SELL":

            position = (
                self.portfolio.positions
                .get(order.symbol)
            )

            if position is None:
                return False

            if (
                position.quantity
                < order.quantity
            ):
                return False

            realized_pnl = (
                (
                    order.price
                    -
                    position.average_entry_price
                )
                *
                order.quantity
            )

            self.portfolio.realized_pnl += (
                realized_pnl
            )

            position.quantity -= (
                order.quantity
            )

            self.portfolio.cash_balance += (
                notional
            )

            if position.quantity == 0:

                del self.portfolio.positions[
                    order.symbol
                ]

        else:
            return False

        self.executed_orders.append(
            order
        )

        return True