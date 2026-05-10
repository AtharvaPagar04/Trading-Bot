from src.execution.exchange_type import (
    ExchangeType,
)

from src.paper_execution.paper_execution_engine import (
    PaperExecutionEngine,
)

from src.execution.binance_execution_engine import (
    BinanceExecutionEngine,
)


def build_execution_engine(
    exchange_type: ExchangeType,
    runtime,
):

    if (
        exchange_type
        ==
        ExchangeType.PAPER
    ):

        return (
            PaperExecutionEngine(
                runtime
            )
        )

    if (
        exchange_type
        ==
        ExchangeType.BINANCE
    ):

        return (
            BinanceExecutionEngine(
                runtime
            )
        )

    raise ValueError(
        "Unsupported exchange type"
    )
