import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

from . import get_random_y4m

DRIVER_PATH = os.path.join("./drivers", "chromium.chromedriver")


def get_browser(y4m=None):
    y4m_file = y4m or get_random_y4m()
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
    # options.set_headless()
    browser = webdriver.Chrome(
            executable_path = DRIVER_PATH,
            # desired_capabilities = webdriver.DesiredCapabilities.CHROME,
            options = options,
        )
    return browser


def run(room, y4m, lifetime=360):
    browser = get_browser(y4m=y4m)
    browser.get(f'https://meet.jit.si/{room}')
    browser.find_element_by_class_name('action-btn').click()
    time.sleep(360)
    try:
        browser.close()
    except NoSuchWindowException as e:
        print('Browser already closed.')
