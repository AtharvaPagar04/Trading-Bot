BALANCE_DRIFT_TOLERANCE = 0.0001


def detect_balance_drift(
    runtime_balances: dict,
    exchange_balances: dict,
):

    drift = {}

    assets = set(
        runtime_balances.keys()
    ).union(
        exchange_balances.keys()
    )

    for asset in assets:

        runtime_total = (
            runtime_balances
            .get(asset, {})
            .get("total", 0)
        )

        exchange_total = (
            exchange_balances
            .get(asset, {})
            .get("total", 0)
        )

        difference = abs(
            runtime_total
            -
            exchange_total
        )

        if (
            difference
            >
            BALANCE_DRIFT_TOLERANCE
        ):

            drift[asset] = {
                "runtime":
                runtime_total,

                "exchange":
                exchange_total,

                "difference":
                difference,
            }

    return drift
