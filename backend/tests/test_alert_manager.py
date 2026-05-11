from src.monitoring.alert_manager import (
    AlertManager,
)


def test_alert_manager():

    manager = (
        AlertManager()
    )

    manager.trigger_alert(
        "disconnect"
    )

    assert (
        len(
            manager.active_alerts()
        )
        ==
        1
    )
