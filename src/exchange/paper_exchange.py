import uuid
from datetime import datetime
from src.exchange.fees import (
    calculate_execution_fee,
)
from src.exchange.slippage import (
    apply_slippage,
)

from src.exchange.spread import (
    apply_spread,
)
from src.exchange.models import (
    Balance,
    CompletedTrade,
    Order,
    OrderSide,
    OrderStatus,
    Position,
)


class PaperExchange:

    def __init__(
        self,
        starting_capital: float,
    ):

        self.balance = Balance(
            total_capital=
            starting_capital,

            available_capital=
            starting_capital,
        )
        self.fee_rate = 0.001
        self.slippage_percent = 0.002
        self.positions = {}
        self.spread_percent = 0.002
        self.completed_trades = []

        self.orders = []

    def execute_market_order(
        self,

        symbol: str,

        side: OrderSide,

        quantity: float,

        price: float,
    ) -> Order:

        order = Order(
            order_id=str(uuid.uuid4()),

            symbol=symbol,

            side=side,

            quantity=quantity,

            price=price,

            status=
            OrderStatus.FILLED,

            timestamp=
            datetime.utcnow(),
        )
        spread = (
            apply_spread(
                market_price=
                price,

                spread_percent=
                self.spread_percent,

                side=side,
            )
        )

        price = (
            spread
            .adjusted_price
        )
        
        slippage = (
            apply_slippage(
                price=price,

                slippage_percent=
                self.slippage_percent,

                side=side,
            )
        )

        price = (
            slippage
            .slipped_price
        )

        cost = quantity * price
        buy_fee = (
            calculate_execution_fee(
                quantity=
                quantity,

                price=
                price,

                fee_rate=
                self.fee_rate,
            )
        )

        if side == OrderSide.BUY:

            self.balance.available_capital -= (
                cost
                +
                buy_fee.fee_paid
            )

            if (
                symbol
                not in self.positions
            ):

                self.positions[symbol] = (
                    Position(
                        symbol=symbol,

                        quantity=
                        quantity,

                        average_price=
                        price,
                    )
                )

            else:

                position = (
                    self.positions[
                        symbol
                    ]
                )

                total_quantity = (
                    position.quantity
                    + quantity
                )

                weighted_price = (
                    (
                        position.quantity
                        *
                        position.average_price
                    )
                    +
                    (
                        quantity
                        * price
                    )
                ) / total_quantity

                position.quantity = (
                    total_quantity
                )

                position.average_price = (
                    weighted_price
                )

        elif side == OrderSide.SELL:
            slippage = (
                apply_slippage(
                    price=price,

                    slippage_percent=
                    self.slippage_percent,

                    side=side,
                )
            )

            price = (
                slippage
                .slipped_price
            )
            
            sell_fee = (
                calculate_execution_fee(
                    quantity=
                    quantity,

                    price=
                    price,

                    fee_rate=
                    self.fee_rate,
                )
            )

            self.balance.available_capital += (
                cost
                -
                sell_fee.fee_paid
            )

            if (
                symbol
                in self.positions
            ):

                position = (
                    self.positions[
                        symbol
                    ]
                )

                entry_price = (
                    position.average_price
                )

                gross_pnl = (
                    (
                        price
                        -
                        entry_price
                    )
                    * quantity
                )

                total_fees = (
                    sell_fee.fee_paid
                )

                realized_pnl = (
                    gross_pnl
                    -
                    total_fees
                )

                position.quantity -= (
                    quantity
                )

                completed_trade = (
                    CompletedTrade(
                        symbol=symbol,

                        quantity=quantity,

                        entry_price=
                        entry_price,

                        exit_price=
                        price,

                        realized_pnl=
                        realized_pnl,

                        opened_at=
                        order.timestamp,
                        fees_paid=
                        total_fees,
                        
                        closed_at=
                        datetime.utcnow(),
                    )
                )

                self.completed_trades.append(
                    completed_trade
                )

                if (
                    position.quantity
                    <= 0
                ):

                    del self.positions[
                        symbol
                    ]

        self.orders.append(order)

        return order