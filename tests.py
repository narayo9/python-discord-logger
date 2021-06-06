import logging
import os

from logger.utils import get_discord_logger


def initialize_logger() -> logging.Logger:
    logger = get_discord_logger(
        __name__,
        os.environ['WEBHOOK_URL'],
        os.environ['WEBHOOK_USER_ID'],
    )
    logger.setLevel(logging.DEBUG)
    return logger


def test_log():
    logger = initialize_logger()
    logger.info("sample info message.")
    logger.warning("sample warning message.")
    logger.error("sample error message.")
