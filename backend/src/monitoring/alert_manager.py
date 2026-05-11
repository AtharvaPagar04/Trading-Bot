class AlertManager:

    def __init__(
        self,
    ):

        self.alerts = []

    def trigger_alert(
        self,
        message: str,
    ):

        self.alerts.append(
            message
        )

    def active_alerts(
        self,
    ):

        return (
            self.alerts
        )
