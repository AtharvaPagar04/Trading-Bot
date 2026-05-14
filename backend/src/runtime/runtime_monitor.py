from src.runtime.governed_runtime import (
    GovernedRuntime,
)
from src.exchange.paper_exchange import (
    PaperExchange,
)
from src.runtime.logging.runtime_logger import (
    runtime_log,
    LogLevel,
    LogCategory,
)

class RuntimeMonitor:

    def __init__(
        self,
        runtime: GovernedRuntime,
        exchange: PaperExchange,
    ):

        self.runtime = runtime
        self.runtime = runtime
        self.exchange = exchange

    def tick(self):

        if not self.runtime.state.is_trading_enabled:
            return

        self.runtime.validate_heartbeat()

        self.runtime.validate_market_data()

        self.runtime.validate_cooldown()
        latest_price = (
            self.runtime.state
            .latest_price
        )

        if latest_price > 0:

            reconciliation_valid = (
                self.exchange
                .portfolio_reconciliation_valid(
                    latest_price=
                    latest_price,
                )
            )

            if not reconciliation_valid:
                
                
                runtime_log(
                    level=LogLevel.WARNING,
                    category=LogCategory.RUNTIME,
                    message=(
                        "Safe mode activated due to "
                        "portfolio reconciliation drift"
                    ),
                )
                self.runtime.activate_safe_mode(
                    reason=(
                        "portfolio reconciliation drift"
                    ),
                )