from src.exchange.models import (
    OrderSide,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

exchange = PaperExchange(
    starting_capital=2000
)

exchange.execute_market_order(
    symbol="SOL/USDT",

    side=OrderSide.BUY,

    quantity=2,

    price=100,
)

exchange.execute_market_order(
    symbol="SOL/USDT",

    side=OrderSide.SELL,

    quantity=2,

    price=110,
)

print("BALANCE")
print(exchange.balance)

print("\nPOSITIONS")
print(exchange.positions)

print("\nCOMPLETED TRADES")
for trade in (
    exchange.completed_trades
):
    print(trade)