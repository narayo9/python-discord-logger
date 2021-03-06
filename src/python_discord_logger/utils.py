__all__ = ["get_discord_logger"]

import logging
import typing

from .formatters import DiscordFormatter
from .handlers import DiscordWebhookHandler


def get_discord_logger(
    name: str, webhook_url: str, username: typing.Optional[str] = None
):
    logger = logging.getLogger(name)
    handler = DiscordWebhookHandler(webhook_url)
    formatter = DiscordFormatter(username)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
