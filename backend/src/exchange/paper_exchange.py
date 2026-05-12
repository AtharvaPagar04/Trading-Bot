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
from src.db.repository import (
    CompletedTradeRepository,
)
from src.db.position_repository import (
    PositionRepository,
)
from src.db.balance_repository import (
    BalanceRepository,
)

class PaperExchange:

    def __init__(
        self,
        starting_capital: float,
        active_session_id: int | None = None,
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
        self.completed_trade_repository = (
            CompletedTradeRepository()
        )
        self.balance_repository = (
            BalanceRepository()
        )
        self.position_repository = (
            PositionRepository()
        )

        self.orders = []

        self.active_session_id = (
            active_session_id
        )

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
            self.balance_repository.save_balance(
                total_capital=
                self.balance.total_capital,

                available_capital=
                self.balance.available_capital,
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
                position = (
                    self.positions[symbol]
                )
                self.position_repository.save_position(
                    symbol=symbol,

                    quantity=position.quantity,

                    average_price=
                    position.average_price,

                    current_price=price,

                    unrealized_pnl=0.0,

                    status="OPEN",
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
                self.position_repository.save_position(
                    symbol=symbol,

                    quantity=position.quantity,

                    average_price=
                    position.average_price,

                    current_price=price,

                    unrealized_pnl=0.0,

                    status="OPEN",
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
            self.balance_repository.save_balance(
                total_capital=
                self.balance.total_capital,

                available_capital=
                self.balance.available_capital,
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
                
                self.completed_trade_repository.save_completed_trade(
                    symbol=
                    completed_trade.symbol,

                    quantity=
                    completed_trade.quantity,

                    entry_price=
                    completed_trade.entry_price,

                    exit_price=
                    completed_trade.exit_price,

                    realized_pnl=
                    completed_trade.realized_pnl,

                    fees_paid=
                    completed_trade.fees_paid,

                    opened_at=
                    completed_trade.opened_at,

                    closed_at=
                    completed_trade.closed_at,
                    
                    session_id=
                    self.active_session_id,
                )

                if (
                    position.quantity
                    <= 0
                ):

                    del self.positions[
                        symbol
                    ]

                    self.position_repository.delete_position(
                        symbol
                    )

        self.orders.append(order)
        return order

    def load_persisted_positions(
        self,
    ):

        positions = (
            self.position_repository
                .get_all_positions()
        )

        for persisted_position in positions:

            self.positions[
                persisted_position.symbol
            ] = Position(
                symbol=
                persisted_position.symbol,

                quantity=
                persisted_position.quantity,

                average_price=
                persisted_position.average_price,
            )

            print(
                f"[RECOVERY] "
                f"Loaded position: "
                f"{persisted_position.symbol}"
            )
    
    def load_persisted_balance(
        self,
    ):

        persisted_balance = (
            self.balance_repository
            .load_balance()
        )

        if persisted_balance:

            self.balance.total_capital = (
                persisted_balance
                .total_capital
            )

            self.balance.available_capital = (
                persisted_balance
                .available_capital
            )

            print(
                "[RECOVERY] "
                "Balance restored"
            )

        