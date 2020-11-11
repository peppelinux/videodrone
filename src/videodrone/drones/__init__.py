# from . import jitsi_chrome

import logging
import os
import warnings
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from videodrone.utils import get_random_y4m


DRIVER_PATH = os.environ.get('VIDEODRONE_DRIVER', 
                             os.path.join("drivers", 
                                          "chromedriver"))


def get_chrome_browser(y4m=None, headless=True):
    y4m_file = get_random_y4m(path=y4m)
    options = webdriver.ChromeOptions()
    # options.add_argument('')
    if headless:
        options.add_argument('--headless')
    options.add_argument('no-sandbox') # otherwise chromedriver in docker env fails ...
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

