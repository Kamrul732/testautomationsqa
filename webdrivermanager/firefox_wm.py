from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Firefox_WDM_config():

    def firefox_wdm_test(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://google.com')

test_obj = Firefox_WDM_config()
test_obj.firefox_wdm_test()