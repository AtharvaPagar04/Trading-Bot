def parse_balances(
    account_payload: dict,
):

    balances = {}

    for balance in (
        account_payload.get(
            "balances",
            [],
        )
    ):

        asset = (
            balance.get(
                "asset"
            )
        )

        free = float(
            balance.get(
                "free",
                0,
            )
        )

        locked = float(
            balance.get(
                "locked",
                0,
            )
        )

        total = (
            free
            +
            locked
        )

        if total > 0:

            balances[asset] = {
                "free": free,
                "locked": locked,
                "total": total,
            }

    return balances
