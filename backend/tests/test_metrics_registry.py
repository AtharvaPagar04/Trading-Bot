from src.monitoring.metrics_registry import (
    MetricsRegistry,
)


def test_metrics_increment():

    registry = (
        MetricsRegistry()
    )

    registry.increment(
        "orders"
    )

    registry.increment(
        "orders"
    )

    assert (
        registry.get_metric(
            "orders"
        )
        ==
        2
    )
