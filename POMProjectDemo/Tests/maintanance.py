import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMProjectDemo.Pages.maintanancePage import MaintenancePage
from POMProjectDemo.Base.testbase import TestBase
from POMProjectDemo.Tests.login import LoginPage
#import HtmlTestRunner

class MaintenanceTest(TestBase):

    def test_01_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_02_verify_password(self):
        driver = self.driver
        driver.find_element_by_link_text("Maintenance").click()
        maintenance = MaintenancePage(driver)
        maintenance.enter_password("admin123")
        maintenance.click_verify()

if __name__ == "__main__":
    unittest.main()