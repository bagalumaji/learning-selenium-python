import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_select_dropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")
    driver.implicitly_wait(10)
    element = driver.find_element(By.ID,"select-demo")
    select = Select(element)
    select.select_by_index(1)
    time.sleep(5)
    select.select_by_value("Wednesday")
    time.sleep(5)
    select.select_by_visible_text("Saturday")
    time.sleep(5)

    driver.quit()

