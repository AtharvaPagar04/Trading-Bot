def requires_reconciliation(
    event: dict,
):

    return (
        event.get(
            "requires_reconciliation",
            False,
        )
    )
