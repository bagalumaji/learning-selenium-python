import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import constants

def test_checkbox():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.URL)
    driver.implicitly_wait(10)
    driver.find_element(By.LINK_TEXT,"Checkbox Demo").click()
    ele = driver.find_element(By.CSS_SELECTOR,"#isAgeSelected")
    if not ele.is_selected():
        ele.click()

    time.sleep(10)

    driver.quit()
