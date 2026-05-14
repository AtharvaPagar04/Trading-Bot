from src.db.database import (
    Base,
    engine,
)

from src.db.models import (
    CandleEntity,
    CompletedTradeEntity,
)
from src.db.position_models import (
    PositionEntity,
)
from src.db.balance_models import (
    BalanceEntity,
)
from src.db.runtime_models import (
    RuntimeStateEntity,
)

from src.db.trading_session_model import (
    TradingSessionModel,
)
from src.db.execution_models import (
    TradeExecutionEntity,
)


def init_db():

    Base.metadata.create_all(
        bind=engine
    )

    print(
        "[DB] Tables created"
    )


if __name__ == "__main__":

    init_db()