from selenium import webdriver

class Firefox_config():
    def firefox_test(self):
        driver = webdriver.Firefox(executable_path="E:\SQA BITM\project\TestAutomation\driver\geckodriver.exe")

test_obj = Firefox_config()
test_obj.firefox_test()