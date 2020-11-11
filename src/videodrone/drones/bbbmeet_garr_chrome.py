from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from . import *

URL = "https://blue.meet.garr.it/"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room='videodrone', y4m='./y4m', lifetime=360, headless=1, pin=None):
    
    browser = get_chrome_browser(y4m=y4m, headless=headless)
    browser.get(f'{URL}/{room}')
    browser.find_element_by_xpath('//*[@id="room_access_code"]').send_keys(pin)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/form/div/input[2]').click()
    browser.find_element_by_xpath('//*[@id="_b_giu-1qd-xfs-muy_join_name"]').send_keys('videodrone')
    browser.find_element_by_id('room-join').click()
    
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]').click()
    time.sleep(5)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/span/button[1]').click()
    
    time.sleep(lifetime)
    # leave the room
    browser.find_element_by_xpath('//*[@id="tippy-3"]/span[1]').click()
    browser.find_element_by_xpath('//*[@id="app"]/main/section/div[1]/header/div/div[1]/div[3]/div/div/div/ul/li[8]').click()
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
