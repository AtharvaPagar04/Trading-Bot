from src.logging.runtime_logger import (
    build_logger,
)


def test_build_logger():

    logger = (
        build_logger(
            "runtime"
        )
    )

    assert (
        logger.name
        ==
        "runtime"
    )
