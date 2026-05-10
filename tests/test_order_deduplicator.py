from src.execution.order_deduplicator import (
    OrderDeduplicator,
)


def test_order_deduplicator():

    dedup = (
        OrderDeduplicator()
    )

    assert (
        dedup.is_duplicate(
            "abc"
        )
        is False
    )

    assert (
        dedup.is_duplicate(
            "abc"
        )
        is True
    )
