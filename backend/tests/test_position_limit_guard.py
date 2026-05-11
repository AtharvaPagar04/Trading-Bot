from src.risk.position_limit_guard import (
    exceeds_position_limit,
)


def test_position_limit_guard():

    result = (
        exceeds_position_limit(
            position_size=5,
            max_position_size=2,
        )
    )

    assert (
        result
        is True
    )
