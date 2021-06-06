import logging
import os

from src.python_discord_logger.utils import get_discord_logger


def initialize_logger() -> logging.Logger:
    logger = get_discord_logger(
        __name__,
        os.environ["WEBHOOK_URL"],
        os.environ["WEBHOOK_USER_ID"],
    )
    logger.setLevel(logging.DEBUG)
    return logger


logger = initialize_logger()


def test_log():
    logger.info("sample info message.")
    logger.warning("sample warning message.")
    logger.error("sample error message.")


def test_exception_log():
    try:
        raise ValueError("sample error happened")
    except ValueError as e:
        logger.error("sample exception error message", exc_info=e)
