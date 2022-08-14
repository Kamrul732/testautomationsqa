from selenium import webdriver

class Chrome_config():
    def chrome_test(self):
        driver = webdriver.Chrome(executable_path="E:\SQA BITM\project\TestAutomation\driver\chromedriver.exe")



test_obj = Chrome_config()
test_obj.chrome_test()