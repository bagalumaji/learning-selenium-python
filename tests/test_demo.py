from selenium import webdriver


def test_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    print(driver.title)

    driver.quit()