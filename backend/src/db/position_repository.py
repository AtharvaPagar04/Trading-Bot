from src.db.database import (
    SessionLocal,
)

from src.db.position_models import (
    PositionEntity,
)


class PositionRepository:

    def __init__(self):

        self.session = (
            SessionLocal()
        )

    def save_position(
        self,
        symbol: str,
        quantity: float,
        average_price: float,
        current_price: float,
        unrealized_pnl: float,
        status: str,
    ):

        existing_position = (
            self.session.query(
                PositionEntity
            )
            .filter_by(
                symbol=symbol
            )
            .first()
        )

        if existing_position:

            existing_position.quantity = (
                quantity
            )

            existing_position.average_price = (
                average_price
            )

            existing_position.current_price = (
                current_price
            )

            existing_position.unrealized_pnl = (
                unrealized_pnl
            )

            existing_position.status = (
                status
            )

        else:

            position = (
                PositionEntity(
                    symbol=symbol,

                    quantity=quantity,

                    average_price=
                    average_price,

                    current_price=
                    current_price,

                    unrealized_pnl=
                    unrealized_pnl,

                    status=status,
                )
            )

            self.session.add(
                position
            )

        self.session.commit()

    def get_all_positions(
        self,
    ):

        return (
            self.session.query(
                PositionEntity
            ).all()
        )

    def delete_position(
        self,
        symbol: str,
    ):

        position = (
            self.session.query(
                PositionEntity
            )
            .filter_by(
                symbol=symbol
            )
            .first()
        )

        if position:

            self.session.delete(
                position
            )

            self.session.commit()

    def get_position(
        self,
        symbol: str,
    ):

        return (
            self.session.query(
                PositionEntity
            )
            .filter_by(
                symbol=symbol
            )
            .first()
    )
    def cleanup_duplicate_positions(
        self,
    ):

        positions = (
            self.session.query(
                PositionEntity
        ).all()
        )

        seen_symbols = set()

        for position in positions:

            if (
                position.symbol
                in seen_symbols
            ):

                self.session.delete(
                    position
                )

            else:

                seen_symbols.add(
                    position.symbol
                )

        self.session.commit()