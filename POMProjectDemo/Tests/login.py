import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMProjectDemo.Pages.loginPage import LoginPage
from POMProjectDemo.Base.testbase import TestBase
from POMProjectDemo.Pages.homePage import HomePage
#import HtmlTestRunner

class LoginTest(TestBase):

    def test_01_login_validation(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials123")

if __name__ == "__main__":
    unittest.main()