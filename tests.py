import logging
import os

from logger.utils import get_discord_logger


def initialize_logger() -> logging.Logger:
    logger = get_discord_logger(
        __name__,
        "https://discord.com/api/webhooks/850999091110346823/aYUhLILjxqzaEtN9R437iOAQq6PLneVucAGMAm4mgRbNIatHp9rViNwYNaSJRgFd6Yxr",
        "258609485155663884",
    )
    logger.setLevel(logging.DEBUG)
    return logger


def test_log():
    logger = initialize_logger()
    logger.info("sample info message.")
    logger.warning("sample warning message.")
    logger.error("sample error message.")
