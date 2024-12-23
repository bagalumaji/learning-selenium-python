import time

from selenium.webdriver.common.by import By

from driver.driver import Driver
from driver.drivermanager import DriverManager


def test_frame():
    Driver.init_driver()
    driver = DriverManager.get_driver()
    driver.get("https://www.lambdatest.com/selenium-playground/iframe-demo/")
    print(driver.title)
    time.sleep(5)
    frame_element = driver.find_element(By.ID,"iFrame1")
    time.sleep(5)
    driver.switch_to.frame(frame_element)
    time.sleep(5)
    text_of_ele = driver.find_element(By.XPATH,"//div[text()='Your content.']").text
    time.sleep(5)
    print(text_of_ele)
    time.sleep(10)
    Driver.quit_driver()