from src.runtime.governed_runtime import (
    GovernedRuntime,
)

from src.paper_execution.paper_order import (
    PaperOrder,
)

from src.paper_execution.paper_portfolio import (
    PaperPortfolio,
)
from datetime import (
    datetime,
    timedelta,
)
from src.execution.execution_interface import (
    ExecutionInterface,
)
from src.paper_execution.paper_position import (
    PaperPosition,
)
from src.paper_execution.order_status import (
    OrderStatus,
)
from src.paper_execution.order_status import (
    OrderStatus,
)

class PaperExecutionEngine(
    ExecutionInterface
):

    def __init__(
        self,
        runtime: GovernedRuntime,

        fee_percent: float = 0.001,

        slippage_percent: float = 0.0005,
        spread_percent: float = 0.0002,
        max_fill_ratio: float = 1.0,
        execution_latency_seconds: int = 0,
        order_expiration_seconds: int = 300,
        
        

    ):

        self.runtime = runtime

        self.fee_percent = (
            fee_percent
        )

        self.slippage_percent = (
            slippage_percent
        )

        self.spread_percent = (
            spread_percent
        )

        self.max_fill_ratio = (
            max_fill_ratio
        )
        self.execution_latency_seconds = (
            execution_latency_seconds
        )
        self.order_expiration_seconds = (
            order_expiration_seconds
        )

        self.executed_orders = []
        self.pending_orders = []

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
            order.status = (
                OrderStatus.REJECTED
            )
            return False

        execution_price = (
            order.price
        )

        half_spread = (
            self.spread_percent
            / 2
        )

        if order.side == "BUY":

            execution_price *= (
                1
                +
                half_spread
                +
                self.slippage_percent
            )

        elif order.side == "SELL":

            execution_price *= (
                1
                -
                half_spread
                -
                self.slippage_percent
            )
            
        if (
            self.execution_latency_seconds
            > 0
        ):

            order.eligible_execution_time = (
                order.timestamp
                +
                timedelta(
                    seconds=
                    self.execution_latency_seconds
                )
            )

        else:

            order.eligible_execution_time = (
                order.timestamp
            )  
        order.expiration_time = (
            order.timestamp
            +
            timedelta(
                seconds=
                self.order_expiration_seconds
            )
        )
    
        filled_quantity = (
            order.quantity
            *
            self.max_fill_ratio
        )
        
        notional = (
            filled_quantity
            *
            execution_price
        )

        fee = (
            notional
            *
            self.fee_percent
        )

        if order.side == "BUY":

            total_cost = (
                notional
                +
                fee
            )

            if (
                self.portfolio.cash_balance
                < total_cost
            ):
                order.status = (
                    OrderStatus.REJECTED
                )
                return False

            self.portfolio.cash_balance -= (
                total_cost
            )

            self.portfolio.fees_paid += (
                fee
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

            existing_quantity = (
                position.quantity
            )

            existing_notional = (
                existing_quantity
                *
                position.average_entry_price
            )

            new_notional = (
                filled_quantity
                *
                execution_price
            )

            new_total_quantity = (
                existing_quantity
                +
                filled_quantity
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
                order.status = (
                    OrderStatus.REJECTED
                )
                return False

            if (
                position.quantity
                < filled_quantity
            ):
                order.status = (
                    OrderStatus.REJECTED
                )
                return False

            realized_pnl = (
                (
                    execution_price
                    -
                    position.average_entry_price
                )
                *
                filled_quantity
            )

            self.portfolio.realized_pnl += (
                realized_pnl
            )

            position.quantity -= (
                filled_quantity
            )

            self.portfolio.cash_balance += (
                notional
                -
                fee
            )

            self.portfolio.fees_paid += (
                fee
            )

            if position.quantity == 0:

                del self.portfolio.positions[
                    order.symbol
                ]

        else:
            return False

        if (
            filled_quantity
            <
            order.quantity
        ):

            order.status = (
                OrderStatus.PARTIALLY_FILLED
            )
            self.pending_orders.append(
                order
            )

        else:

            order.status = (
                OrderStatus.FILLED
            )

        order.filled_quantity = (
            filled_quantity
        )
        self.executed_orders.append(
            order
        )

        return True
        
    def process_pending_orders(
        self,
    ) -> None:

        completed_orders = []

        for order in (
            self.pending_orders
        ):

            # =========================
            # ORDER EXPIRATION CHECK
            # =========================

            if (
                order.expiration_time
                is not None
            ):

                if (
                    datetime.utcnow()
                    >=
                    order.expiration_time
                ):

                    order.status = (
                        OrderStatus.CANCELLED
                    )

                    completed_orders.append(
                        order
                    )

                    continue

            # =========================
            # EXECUTION LATENCY CHECK
            # =========================

            if (
                order.eligible_execution_time
                is not None
            ):

                if (
                    datetime.utcnow()
                    <
                    order.eligible_execution_time
                ):

                    continue

            # =========================
            # CONTINUE PARTIAL FILL
            # =========================

            remaining = (
                order.quantity
                -
                order.filled_quantity
            )

            additional_fill = (
                remaining
                *
                self.max_fill_ratio
            )

            order.filled_quantity += (
                additional_fill
            )

            # =========================
            # FULLY FILLED CHECK
            # =========================

            if (
                order.filled_quantity
                >=
                order.quantity
            ):

                order.filled_quantity = (
                    order.quantity
                )

                order.status = (
                    OrderStatus.FILLED
                )

                completed_orders.append(
                    order
                )

        # =========================
        # REMOVE COMPLETED ORDERS
        # =========================

        for order in completed_orders:

            self.pending_orders.remove(
                order
            )

    def cancel_order(
        self,
        order: PaperOrder,
    ) -> bool:

        if (
            order
            not in
            self.pending_orders
        ):

            return False

        self.pending_orders.remove(
            order
        )

        order.status = (
            OrderStatus.CANCELLED
        )

        return True