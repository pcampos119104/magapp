import functools
import logging

logger = logging.getLogger(__name__)


def log_start(f):
    """
    Log the start of a function with this annotation.
    used on pycharm to refactor, many function at once
    The regex to capture: ([ ]*)(def (?!__init__)\\w+) # noqa W605
    The regex to replace: $1@log_start \n$1$2
    """

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        logger.info(f"START: {f.__module__} {f.__name__}")
        return f(*args, **kwargs)

    return wrapped
