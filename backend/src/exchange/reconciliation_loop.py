from src.exchange.drift_detector import (
    detect_balance_drift,
)

from src.monitoring.metrics_registry import (
    MetricsRegistry,
)

from src.monitoring.alert_manager import (
    AlertManager,
)

from src.logging.runtime_logger import (
    build_logger,
)


class ReconciliationLoop:

    def __init__(
        self,
        runtime_portfolio: dict,
        exchange_balances: dict,
        runtime=None,

    ):

        self.runtime_portfolio = (
            runtime_portfolio
        )

        self.exchange_balances = (
            exchange_balances
        )

        self.metrics = (
            MetricsRegistry()
        )
        self.runtime = runtime
        self.alerts = (
            AlertManager()
        )

        self.logger = (
            build_logger(
                "reconciliation"
            )
        )

    def run_cycle(
        self,
    ):

        self.logger.info(
            "Running reconciliation cycle"
        )

        self.metrics.increment(
            "reconciliation_cycles"
        )

        drift = (
            detect_balance_drift(
                self.runtime_portfolio,
                self.exchange_balances,
            )
        )

        if len(drift) > 0:
            
            if (
                self.runtime
                is not None
            ):

                self.runtime.activate_safe_mode(
                    reason=(
                        "reconciliation drift detected"
                    ),
                )

            self.metrics.increment(
                "drift_events"
            )

            self.alerts.trigger_alert(
                "Balance drift detected"
            )

            self.logger.warning(
                "Balance drift detected"
            )

        return drift
