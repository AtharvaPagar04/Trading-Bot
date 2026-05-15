from src.runtime.event_journal import (
    EventJournal,
)
from src.runtime.logging.runtime_loggers import (
    runtime_logger as logger,
)

journal = EventJournal()




class RuntimeInstrumentation:

    @staticmethod
    def track_event(
        event_type: str,
        payload: dict,
    ):

        logger.info(
            (
                f"{event_type} | "
                f"{payload}"
            )
        )

        journal.log_event(
            event_type=
            event_type,

            payload=
            payload,
        )