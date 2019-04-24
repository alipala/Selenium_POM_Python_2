import unittest
from selenium import webdriver
import datetime

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/_D/python-misc/drivers/chromedriver.exe")
        print("-----------------------------------------")
        print("Test started")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        if cls.driver != None:
            print("-----------------------------------------")
            print("Tests finished")
            cls.driver.close()
            cls.driver.quit()