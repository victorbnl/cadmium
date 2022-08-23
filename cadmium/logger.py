import logging


def getLogger(name):
    """Get a logger with module name."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    return logger
