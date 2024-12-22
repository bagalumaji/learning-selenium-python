import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_click_send_keys():
    driver  = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    driver.find_element(By.NAME,"q").send_keys("Umaji Bagal",Keys.ENTER)
    # driver.find_element(By.NAME,"q").send_keys()
    time.sleep(10)
    driver.quit()