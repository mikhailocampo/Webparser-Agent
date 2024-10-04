import logging
from loguru import logger
from typing import List


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging(
    logging_level: int, loggers: List[str] = ("uvicorn.asgi", "uvicorn.access")
) -> None:
    # Remove default handler
    logger.remove()

    # Add default handler with specified level
    logger.add(sink=lambda msg: print(msg), level=logging_level)

    # Intercept standard logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0)

    # Update logger levels
    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False
        logging_logger.level = logging_level
