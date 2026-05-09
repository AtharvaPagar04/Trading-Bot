from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
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

            current_position = (
                self.portfolio.positions
                .get(order.symbol, 0.0)
            )

            self.portfolio.positions[
                order.symbol
            ] = (
                current_position
                +
                order.quantity
            )

        elif order.side == "SELL":

            current_position = (
                self.portfolio.positions
                .get(order.symbol, 0.0)
            )

            if (
                current_position
                < order.quantity
            ):
                return False

            self.portfolio.positions[
                order.symbol
            ] = (
                current_position
                -
                order.quantity
            )

            self.portfolio.cash_balance += (
                notional
            )

        else:
            return False

        self.executed_orders.append(
            order
        )

        return True