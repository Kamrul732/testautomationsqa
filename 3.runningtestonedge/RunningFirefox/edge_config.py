from selenium import webdriver

class Edge_config():
    def edge_test(self):
        driver = webdriver.Edge(executable_path="E:\SQA BITM\project\TestAutomation\driver\msedgedriver.exe")

test_obj = Edge_config()
test_obj.edge_test()