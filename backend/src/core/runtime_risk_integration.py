from dataclasses import dataclass

from src.core.runtime import (
    RuntimeState,
)

from src.core.runtime_transition_engine import (
    execute_runtime_transition,
)

from src.core.runtime_state_machine import (
    RuntimeOperatingState,
)

from src.exchange.portfolio_risk import (
    PortfolioRiskLevel,
    PortfolioRiskState,
)


@dataclass
class RuntimeRiskIntegrationResult:
    runtime: RuntimeState

    execution_allowed: bool


def integrate_portfolio_risk(
    runtime: RuntimeState,

    portfolio_risk:
    PortfolioRiskState,
) -> RuntimeRiskIntegrationResult:

    execution_allowed = (
        portfolio_risk
        .allow_new_entries
    )

    if (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .CRITICAL
    ):

        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .HALTED,
        )

    elif (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .HIGH_RISK
    ):

        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .REDUCE_RISK,
        )

    elif (
        portfolio_risk
        .risk_level
        ==
        PortfolioRiskLevel
        .CAUTION
    ):

        execute_runtime_transition(
            runtime=runtime,

            target_state=
            RuntimeOperatingState
            .RECOVERY,
        )

    return RuntimeRiskIntegrationResult(
        runtime=runtime,

        execution_allowed=
        execution_allowed,
    )