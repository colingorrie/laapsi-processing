import logging
from pypyr.context import Context

from scripts.add_exposures import add_exposures

# getLogger will grab the parent logger context, so your loglevel and
# formatting automatically will inherit correctly from the pypyr core.
logger = logging.getLogger(__name__)


def run_step(context: Context) -> None:
    """Put your code in here. This shows you how to code a custom pipeline step.

    Args:
      context: dict-like. This is the entire pypyr context.
               You can mutate context in this step to make
               keys/values & data available to subsequent
               pipeline steps.

    Returns:
      None.
    """
    logger.debug("started")

    logger.info("add_exposures")
    add_exposures()

    logger.debug("done")