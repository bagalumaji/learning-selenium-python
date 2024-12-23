from selenium.webdriver.chrome.webdriver import WebDriver
import threading


class DriverManager:
    """
    A thread-safe manager for storing and retrieving WebDriver instances.
    """
    _driver = threading.local()

    @staticmethod
    def set_driver(driver: WebDriver) -> None:
        """
        Sets the WebDriver instance for the current thread.
        :param driver: WebDriver instance to be managed.
        """
        DriverManager._driver.instance = driver

    @staticmethod
    def get_driver(default: WebDriver = None) -> WebDriver:
        """
        Retrieves the WebDriver instance for the current thread.
        :param default: The default value to return if no driver is set.
        :return: The WebDriver instance or the provided default.
        """
        return getattr(DriverManager._driver, 'instance', default)

    @staticmethod
    def unload() -> None:
        """
        Unloads the WebDriver instance for the current thread.
        """
        if hasattr(DriverManager._driver, 'instance'):
            del DriverManager._driver.instance