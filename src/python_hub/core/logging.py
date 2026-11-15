"""Logging configuration helpers."""

from __future__ import annotations

import logging


def configure_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure and return the application logger.

    The function is idempotent and does not replace handlers installed by callers.
    """
    logger = logging.getLogger("python_hub")
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%H:%M:%S",
            )
        )
        logger.addHandler(handler)

    logger.propagate = False
    return logger
