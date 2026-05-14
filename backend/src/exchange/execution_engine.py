from src.db.database import (
    SessionLocal,
)

from src.db.position_models import (
    PositionEntity,
)

from src.db.execution_models import (
    TradeExecutionEntity,
)

class ExecutionEngine:

    def __init__(self):

        self.session = (
            SessionLocal()
        )

    def open_position(
        self,
        symbol: str,
        side: str,
        quantity: float,
        entry_price: float,
    ):

        position = (
            PositionEntity(
                symbol=symbol,

                side=side,

                quantity=quantity,

                average_price=
                entry_price,

                status="OPEN",
            )
        )

        self.session.add(
            position
        )

        self.session.commit()

        return position

    def close_position(
        self,
        position_id: int,
        exit_price: float,
    ):

        position = (
            self.session.query(
                PositionEntity
            )
            .filter_by(
                id=position_id
            )
            .first()
        )

        if position is None:

            return None

        pnl = (
            (
                exit_price
                -
                position.average_price
            )
            *
            position.quantity
        )

        execution = (
            TradeExecutionEntity(
                symbol=
                position.symbol,

                side=
                position.side,

                quantity=
                position.quantity,

                price=
                exit_price,

                realized_pnl=
                pnl,
            )
        )

        position.status = (
            "CLOSED"
        )

        self.session.add(
            execution
        )

        self.session.commit()

        return execution

    def get_positions(self):

        return (
            self.session.query(
                PositionEntity
            ).all()
        )

    def get_executions(self):

        return (
            self.session.query(
                TradeExecutionEntity
            ).all()
        )