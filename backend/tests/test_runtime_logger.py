from src.logging.runtime_logger import (
    create_logger,
)


def test_create_logger():

    logger = (
        create_logger(
            "runtime"
        )
    )

    assert (
        logger.name
        ==
        "runtime"
    )
