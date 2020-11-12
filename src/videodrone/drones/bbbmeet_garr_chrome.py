from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

from . import *

URL = "https://blue.meet.garr.it"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room='videodrone', y4m='./y4m', lifetime=360, headless=1, pin=None):
    
    browser = get_chrome_browser(y4m=y4m, headless=headless)
    browser.get(f'{URL}/{room}')
    browser.find_element_by_xpath('//*[@id="room_access_code"]').send_keys(pin)
    browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/form/div/input[2]').click()
    browser.find_element_by_xpath('//*[@id="_b_giu-1qd-xfs-muy_join_name"]').send_keys('videodrone')
    browser.find_element_by_id('room-join').click()
    
    # connection to audio server, this could be lagged
    ui_element = '/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]'
    element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, ui_element)))
    element.click()
    ui_element = '/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]/i'
    element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, ui_element)))
    element.click()
    
    # time.sleep(5)
    # browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]').click()
    # time.sleep(5)
    # browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/span/button[1]').click()
    
    # show cam
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="tippy-25"]/span[1]').click()
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/div/button[2]/span").click()
    
    time.sleep(lifetime)
    # leave the room
    browser.find_element_by_xpath('//*[@id="tippy-3"]/span[1]').click()
    browser.find_element_by_xpath('//*[@id="app"]/main/section/div[1]/header/div/div[1]/div[3]/div/div/div/ul/li[8]').click()
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
