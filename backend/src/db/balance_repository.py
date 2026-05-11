from src.db.database import (
    SessionLocal,
)

from src.db.balance_models import (
    BalanceEntity,
)


class BalanceRepository:

    def __init__(
        self,
    ):

        self.session = (
            SessionLocal()
        )

    def save_balance(
        self,
        total_capital: float,
        available_capital: float,
    ):

        existing_balance = (
            self.session.query(
                BalanceEntity
            ).first()
        )

        if existing_balance:

            existing_balance.total_capital = (
                total_capital
            )

            existing_balance.available_capital = (
                available_capital
            )

        else:

            balance = (
                BalanceEntity(
                    total_capital=
                    total_capital,

                    available_capital=
                    available_capital,
                )
            )

            self.session.add(
                balance
            )

        self.session.commit()

    def load_balance(
        self,
    ):

        return (
            self.session.query(
                BalanceEntity
            ).first()
        )