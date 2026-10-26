from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name, headless):
        if browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)
        elif browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(options=options)
        else:
            raise ValueError(
                f"Неподдерживаемый браузер: {browser_name}. "
                f"Допустимые браузеры: firefox, chrome"
            )
