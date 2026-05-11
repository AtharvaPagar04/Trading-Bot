class DynamicPositionSizer:

    def calculate_size(
        self,
        equity: float,
        market_price: float,
        base_risk_percent: float,
        confidence: float,
        volatility_multiplier: float,
        drawdown_multiplier: float,
    ):

        adjusted_risk = (
            base_risk_percent
            *
            confidence
            *
            volatility_multiplier
            *
            drawdown_multiplier
        )

        capital_to_allocate = (
            equity
            *
            adjusted_risk
        )

        quantity = (
            capital_to_allocate
            /
            market_price
        )

        print()

        print(
            "ADJUSTED RISK"
        )

        print(
            adjusted_risk
        )

        print()

        print(
            "ALLOCATED CAPITAL"
        )

        print(
            capital_to_allocate
        )

        return quantity