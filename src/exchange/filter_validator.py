def validate_min_notional(
    quantity: float,
    price: float,
    min_notional: float,
):

    notional = (
        quantity
        *
        price
    )

    return (
        notional
        >=
        min_notional
    )
