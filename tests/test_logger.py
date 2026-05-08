from src.logging.logger import StructuredLogger


def test_logger_creation():

    logger = StructuredLogger()

    assert logger is not None


def test_log_event():

    logger = StructuredLogger()

    logger.log_event(
        event_type="TEST_EVENT",
        message="test message",
        payload={
            "value": 123
        },
    )

    assert True