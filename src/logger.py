import logging
from constants import LogLevel

logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.DEBUG)

def log(message: str, logging_level: LogLevel) -> None:
    """
    Simple log function to handle debugging.
    """
    if logging_level == LogLevel.INFO:
        logging.info(message)
    elif logging_level == LogLevel.DEBUG:
        logging.debug(message)
    elif logging_level == LogLevel.WARNING:
        logging.warning(message)
    elif logging_level == LogLevel.ERROR:
        logging.error(message)



