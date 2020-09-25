import glob
import logging
import random

logger = logging.getLogger(__name__)


def get_random_y4m(path='/tmp/y4ms'):
    y4ms = [i for i in glob.iglob(f'{path}/*y4m')]
    if not y4ms: 
        logger.warning(f'WARNING: y4ms folder is empty: {path}')
    return random.choices(y4ms)[0]
