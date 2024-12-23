from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver():
        """
        Return a WebDriver instance based on the browser name in the configuration.
        """
        browser_name = "chrome"

        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise Exception(f"{browser_name} is an invalid browser name.")
