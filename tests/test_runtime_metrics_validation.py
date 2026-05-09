from src.runtime.metrics import (
    RuntimeMetrics,
)


def test_metric_increment():

    metrics = RuntimeMetrics()

    metrics.increment(
        "trades_executed"
    )

    metrics.increment(
        "trades_executed"
    )

    assert (
        metrics.get_metric(
            "trades_executed"
        )
        ==
        2
    )


def test_metric_report():

    metrics = RuntimeMetrics()

    metrics.increment(
        "risk_alerts",
        value=3,
    )

    report = (
        metrics.report()
    )

    assert (
        report["risk_alerts"]
        ==
        3
    )


def test_unknown_metric_returns_zero():

    metrics = RuntimeMetrics()

    assert (
        metrics.get_metric(
            "unknown_metric"
        )
        ==
        0
    )