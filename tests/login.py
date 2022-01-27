from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:/python/selenium/drivers/firefox/geckodriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_login_valid(self):
        self.driver.get("https:seersco.dev/login")
        self.driver.find_element_by_xpath("/html/body/div[1]/header/div/div/div[1]/div/nav/div/ul/li[4]/a").click()
        self.driver.find_element_by_id("email").send_keys("usman.ghani+324@seersco.com")
        self.driver.find_element_by_id("password").send_keys("usmanghani324")
        time.sleep(2)

    @classmethod

    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit() 
        print("Test completed")    