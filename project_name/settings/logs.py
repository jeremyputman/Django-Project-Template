# Django Imports
import logging
import sys

# Third Party Imports
from loguru import logger  # type: ignore

logger.remove()  # remove default handler
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level}</level> | "
        "<yellow>{extra[method]}</yellow> "
        "<yellow>{extra[http_version]}</yellow> "
        "<yellow>{extra[path]}</yellow> | "
        "<cyan>user={extra[user]}</cyan> "
        "<magenta>ip={extra[ip]}</magenta> | "
        "<blue>{name}:{function}:{line}</blue> - "
        "{message}"
    ),
)

logger.add(
    "logs/appfactory.log",
    level="DEBUG",
    rotation="10 MB",
    retention="14 days",
    compression="zip",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {extra[method]} {extra[http_version]} {extra[path]} | "
        "user={extra[user]} ip={extra[ip]} | "
        "{name}:{function}:{line} - {message}"
    ),
    enqueue=True,  # safe for multi-thread / multi-process
)

logging.basicConfig(handlers=[logging.NullHandler()])
