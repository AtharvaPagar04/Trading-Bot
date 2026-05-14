from src.db.database import (
    SessionLocal,
)

from src.db.runtime_models import (
    RuntimeStateEntity,
)
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)

class RuntimeRepository:

    def __init__(
        self,
    ):

        self.session = (
            SessionLocal()
        )

    def save_runtime_state(
        self,
        operating_state: str,
        safe_mode: bool,
        total_trades: int,
    ):

        existing_state = (
            self.session.query(
                RuntimeStateEntity
            ).first()
        )

        if existing_state:

            existing_state.operating_state = (
                operating_state
            )

            existing_state.safe_mode = (
                safe_mode
            )

            existing_state.total_trades = (
                total_trades
            )

        else:

            runtime_state = (
                RuntimeStateEntity(
                    operating_state=
                    operating_state,

                    safe_mode=
                    safe_mode,

                    total_trades=
                    total_trades,
                )
            )

            self.session.add(
                runtime_state
            )

        self.session.commit()
        runtime_log(
            level=LogLevel.DEBUG,
            category=LogCategory.PERSISTENCE,
            message=(
                "Runtime state persisted"
            ),
        )

    def load_runtime_state(
        self,
    ):

        return (
            self.session.query(
                RuntimeStateEntity
            ).first()
        )