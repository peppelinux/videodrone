import logging
import os
import warnings
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from videodrone.utils import get_random_y4m


DRIVER_PATH = os.environ.get('VIDEODRONE_DRIVER', 
                             os.path.join("drivers", 
                                          "chromium.chromedriver"))
URL = "https://edu.meet.garr.it"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def get_browser(y4m=None):
    y4m_file = get_random_y4m(path=y4m)
    options = webdriver.ChromeOptions()
    # options.add_argument('')
    options.add_argument('--headless')
    # options.add_argument('no-sandbox')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--use-fake-device-for-media-stream')
    options.add_argument('--use-fake-ui-for-media-stream')
    options.add_argument(f'--use-file-for-fake-video-capture={y4m_file}')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(
            executable_path = DRIVER_PATH,
            # desired_capabilities = webdriver.DesiredCapabilities.CHROME,
            options = options,
        )
    return browser


def run(room, y4m, lifetime=360):
    browser = get_browser(y4m=y4m)
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
        print('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
