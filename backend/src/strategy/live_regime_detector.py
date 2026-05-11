import statistics


class LiveRegimeDetector:

    def detect_regime(
        self,
        candles,
    ):

        if len(candles) < 5:

            return "UNKNOWN"

        closes = [
            candle.close
            for candle in candles
        ]

        returns = []

        for i in range(
            1,
            len(closes),
        ):

            change = (
                closes[i]
                -
                closes[i - 1]
            )

            returns.append(change)

        volatility = (
            statistics.stdev(
                returns
            )
            if len(returns) > 1
            else 0
        )

        directional_bias = (
            closes[-1]
            -
            closes[0]
        )

        print()

        print(
            "VOLATILITY:",
            volatility,
        )

        print(
            "DIRECTIONAL BIAS:",
            directional_bias,
        )

        if volatility > 50:

            return "VOLATILE"

        if abs(
            directional_bias
        ) > 100:

            return "TREND"

        return "RANGE"