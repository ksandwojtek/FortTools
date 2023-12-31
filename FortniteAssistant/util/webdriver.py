from selenium import webdriver
from selenium_driver_updater import DriverUpdater
from selenium.webdriver.chrome.service import Service as ChromeService


class Webdriver:
    def __init__(self, headless) -> None:
        self.headless = headless

    def create_webdriver(self):
        driverPath = DriverUpdater.install(path="../..", driver_name=DriverUpdater.chromedriver, upgrade=True,
                                           check_driver_is_up_to_date=True, old_return=False)
        options = self.add_webdriver_options(webdriver.ChromeOptions())
        service = ChromeService(driverPath)
        return webdriver.Chrome(service=service, options=options)

    def add_webdriver_options(self, options):
        options.add_argument("log-level=3")
        options.add_argument("user-data-dir=C:\\Users\\ksand\\AppData\\Local\\Google\\Chrome\\User Data")
        if self.headless:
            options.add_argument("--headless")
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                         "Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
            options.add_argument(f'user-agent={user_agent}')
        return options
