from selenium import webdriver

from driver.drivermanager import DriverManager
from factories.DriverFactory import DriverFactory


class Driver:
    @staticmethod
    def init_driver():
        DriverManager.set_driver(DriverFactory.get_driver())

    @staticmethod
    def quit_driver():
        if driver := DriverManager.get_driver():
            driver.quit()
            DriverManager.unload()