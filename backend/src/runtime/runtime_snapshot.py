from src.exchange.paper_exchange import (
    PaperExchange,
)


def build_runtime_snapshot(
    runtime,
    exchange: PaperExchange,
):

    positions = []
    active_trades = []
    completed_trades = []
    invested_capital = 0.0
    holdings_value = 0.0
    total_unrealized_pnl = 0.0
    total_unrealized_pnl_percent = 0.0

    for symbol, position in (
        exchange.positions.items()
    ):
       
        position_cost = (
            position.quantity
            *
            position.average_price
        )

        position_market_value = (
            position.quantity
            *
            runtime.latest_price
        )

        invested_capital += (
            position_cost
        )

        holdings_value += (
            position_market_value
        )
        
        total_unrealized_pnl += (
            position_market_value
            -
            position_cost
        )

        unrealized_pnl = (
            position_market_value
            -
            position_cost
        )

        unrealized_pnl_percent = (
            (
                runtime.latest_price
                -
                position.average_price
            )
            /
            position.average_price
        ) * 100

        active_trades.append(
            {
                "symbol":
                symbol,

                "status":
                "OPEN",

                "quantity":
                position.quantity,

                "entry_price":
                position.average_price,

                "current_price":
                runtime.latest_price,

                "market_value":
                position_market_value,

                "unrealized_pnl":
                unrealized_pnl,

                "unrealized_pnl_percent":
                unrealized_pnl_percent,
            }
        )

        positions.append(
            {
                "symbol": symbol,

                "quantity":
                position.quantity,

                "average_price":
                position.average_price,
            }
        )

    for trade in (
        exchange.completed_trades
    ):

        completed_trades.append(
            {
                "symbol":
                trade.symbol,

                "quantity":
                trade.quantity,

                "entry_price":
                trade.entry_price,

                "exit_price":
                trade.exit_price,

                "realized_pnl":
                trade.realized_pnl,

                "fees_paid":
                trade.fees_paid,

                "opened_at":
                str(
                    trade.opened_at
                ),

                "closed_at":
                str(
                    trade.closed_at
                ),
            }
        )
    

    return {

        "runtime": {

            "safe_mode":
            runtime.safe_mode,

            "operating_state":
            runtime.operating_state,
        },

        "telemetry": {

            "latest_price":
            runtime.latest_price,

            "latest_candle_close":
            runtime.latest_candle_close,

            "total_trades":
            runtime.total_trades,

            "current_unrealized_pnl":
            runtime.current_unrealized_pnl,

            "current_unrealized_pnl_percent":
            runtime.current_unrealized_pnl_percent,

            "last_execution_price":
            runtime.last_execution_price,

            "last_execution_time":
            (
                str(
                    runtime
                    .last_execution_time
                )
                if runtime
                .last_execution_time
                else None
            ),
        },

        "portfolio": {

            "total_capital":
            exchange.balance
            .total_capital,

            "available_capital":
            exchange.balance
            .available_capital,
            
            "invested_capital":
            invested_capital,

            "holdings_value":
            holdings_value,

            "total_unrealized_pnl":
            total_unrealized_pnl,

            "total_portfolio_value":
            (
                exchange.balance
                .available_capital
                +
                holdings_value
            ),

            "positions":
            positions,
        },
        "active_trades":
        active_trades,
        "trade_journal":
        completed_trades,
    }