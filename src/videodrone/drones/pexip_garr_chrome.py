import random

from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from . import *

URL = "https://web.vconf.garr.it/webapp/conference"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room='videodrone', y4m='./y4m', lifetime=360, 
        headless=1, pin=None, **kwargs):
    num = kwargs.get('id', random.randrange(1000))
    suffix = kwargs.get('suffix', 'default')
    
    url = kwargs.get('url') or URL
    browser = get_chrome_browser(y4m=y4m, headless=headless)
    browser.get(f'{url}/{room}')
    
    time.sleep(3)
    browser.find_element_by_id('display-name-dialog-input').send_keys(f'videodrone-{suffix}-{num}')
    time.sleep(1)
    browser.find_element_by_id('display-name-dialog-ok').click()
    
    time.sleep(3)
    browser.find_element_by_id('dialog-pin-input').send_keys(pin)
    time.sleep(1)
    browser.find_element_by_id('conference-pin-btn').click()
    
    time.sleep(lifetime)
    # leave the room
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
