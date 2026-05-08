import logging


def setup_logger():

    logger = logging.getLogger(
        "trading_runtime"
    )

    logger.setLevel(
        logging.INFO
    )

    if logger.handlers:

        return logger

    formatter = logging.Formatter(
        (
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        )
    )

    file_handler = (
        logging.FileHandler(
            "logs/runtime.log"
        )
    )

    file_handler.setFormatter(
        formatter
    )

    console_handler = (
        logging.StreamHandler()
    )

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )

    return logger