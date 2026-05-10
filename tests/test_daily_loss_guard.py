from src.risk.daily_loss_guard import (
    exceeds_daily_loss,
)


def test_exceeds_daily_loss():

    result = (
        exceeds_daily_loss(
            realized_pnl=-150,
            max_daily_loss=100,
        )
    )

    assert (
        result
        is True
    )
