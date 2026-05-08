from src.exchange.models import (
    OrderSide,
)

from src.exchange.paper_exchange import (
    PaperExchange,
)

exchange = PaperExchange(
    starting_capital=2000
)

buy_order = (
    exchange.execute_market_order(
        symbol="SOL/USDT",

        side=OrderSide.BUY,

        quantity=2,

        price=100,
    )
)

print("BUY ORDER")
print(buy_order)

print("\nBALANCE")
print(exchange.balance)

print("\nPOSITIONS")
print(exchange.positions)

sell_order = (
    exchange.execute_market_order(
        symbol="SOL/USDT",

        side=OrderSide.SELL,

        quantity=1,

        price=110,
    )
)

print("\nSELL ORDER")
print(sell_order)

print("\nBALANCE")
print(exchange.balance)

print("\nPOSITIONS")
print(exchange.positions)