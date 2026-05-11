from src.risk.capital_governance_models import (
    CapitalApproval,
)


class CapitalGovernance:

    def approve_trade(
        self,
        cash_balance: float,
        market_price: float,
        requested_quantity: float,
    ):

        required_cash = (
            market_price
            *
            requested_quantity
        )

        if required_cash <= cash_balance:

            return CapitalApproval(
                approved=True,

                approved_quantity=
                requested_quantity,

                required_cash=
                required_cash,

                available_cash=
                cash_balance,

                rejection_reason=
                None,
            )

        adjusted_quantity = (
            cash_balance
            /
            market_price
        )

        if adjusted_quantity <= 0:

            return CapitalApproval(
                approved=False,

                approved_quantity=0,

                required_cash=
                required_cash,

                available_cash=
                cash_balance,

                rejection_reason=
                "INSUFFICIENT_FUNDS",
            )

        return CapitalApproval(
            approved=True,

            approved_quantity=
            adjusted_quantity,

            required_cash=
            adjusted_quantity
            *
            market_price,

            available_cash=
            cash_balance,

            rejection_reason=
            "POSITION_SIZE_REDUCED",
        )