import logging

from . import *

URL = "https://open.meet.garr.it/"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room, y4m, lifetime=360):
    browser = get_chrome_browser(y4m=y4m)
    browser.get(f'{URL}/{room}')
    time.sleep(lifetime)
    # leave the room
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
