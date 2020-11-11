import logging

from selenium.common.exceptions import NoSuchWindowException
from . import *

logger = logging.getLogger(__name__)


URL = "https://meet.jit.si"
warnings.filterwarnings("ignore", category=UserWarning)


def run(room, y4m, lifetime=360, headless=1, **kwargs):
    browser = get_chrome_browser(y4m=y4m, headless=headless)
    browser.get(f'{URL}/{room}')
    # Deprecation Warning
    browser.find_element_by_class_name('action-btn').click()
    # browser.find_element(value='action-btn', by=By.CLASS_NAME)
    time.sleep(lifetime)
    # leave the room
    browser.find_element_by_class_name('toolbox-button').click()
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
