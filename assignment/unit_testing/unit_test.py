'''
Created on 10-Feb-2024

@author: leand
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    
    def setUp(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(options=opts)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
    def test_navigation(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        opts.add_argument("start_maximized")
        
        expected_page_title="OrangeHRM"
        actual_page_title=self.driver
        
        
        


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()