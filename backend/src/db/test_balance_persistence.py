from src.db.balance_repository import (
    BalanceRepository,
)

repository = (
    BalanceRepository()
)

repository.save_balance(
    total_capital=2000,

    available_capital=1750,
)

balance = (
    repository.load_balance()
)

print(
    balance.total_capital,
    balance.available_capital,
)