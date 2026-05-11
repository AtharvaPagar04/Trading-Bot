from src.runtime.event_journal import (
    EventJournal,
)

from src.runtime.logger import (
    setup_logger,
)

journal = EventJournal()

logger = setup_logger()


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