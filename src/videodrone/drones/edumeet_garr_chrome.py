from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from . import *

URL = "https://edu.meet.garr.it"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room, y4m, lifetime=360, headless=1, **kwargs):
    browser = get_chrome_browser(y4m=y4m, headless=headless)
    browser.get(f'{URL}/{room}')
    browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/button[2]').click()
    # browser.find_element(By.XPATH('/html/body/div[2]/div[3]/div/div[3]/button[2]')).click()
    time.sleep(lifetime)
    # leave the room
    browser.find_element_by_xpath('/html/body/div[1]/div/header/div/button/span[1]').click()
    # browser.find_element(By.XPATH('/html/body/div[1]/div/header/div/button/span[1]')).click()
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
