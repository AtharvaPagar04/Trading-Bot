def exceeds_daily_loss(
    realized_pnl: float,
    max_daily_loss: float,
):

    return (
        abs(realized_pnl)
        >=
        max_daily_loss
    )
