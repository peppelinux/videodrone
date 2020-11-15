import logging

from . import *

URL = "https://open.meet.garr.it/"

logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def run(room, y4m, lifetime=360, headless=1, **kwargs):
    url = kwargs.get('url') or URL
    drone_name = build_drone_name(**kwargs)

    browser = get_chrome_browser(y4m=y4m, headless=headless)
    
    endpoint = f'{url}/{room}'
    logger.info(f'Connecting to {endpoint}')
    browser.get(endpoint)
        
    # change name
    time.sleep(2)
    entity = '/html/body/div/div[1]/div/div[3]/div[2]/div[3]/div[3]/div/div[1]/div/div/div/div'
    browser.find_element_by_xpath(entity).click()
    time.sleep(2)
    entity = '//*[@id="new-toolbox"]/div[2]/div[3]/div/div/div[2]/div/div/ul/li[1]/span[1]/div/img'
    browser.find_element_by_xpath(entity).click()
    time.sleep(2)
    entity = '//*[@id="setDisplayName"]'
    browser.find_element_by_xpath(entity).send_keys(drone_name)
    time.sleep(2)
    entity = '//*[@id="modal-dialog-ok-button"]/span/span'
    browser.find_element_by_xpath(entity).click()
    
    time.sleep(lifetime)
    # leave the room
    try:
        browser.close()
    except NoSuchWindowException as e:
        logging.warning('Browser already closed.')
    logger.info('Drone say goodbye ... Destroyed.')
