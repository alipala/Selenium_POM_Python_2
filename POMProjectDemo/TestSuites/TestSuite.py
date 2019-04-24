import unittest
from POMProjectDemo.Tests.login import LoginTest
from POMProjectDemo.Tests.maintanance import MaintenanceTest
import HtmlTestRunner
import os

# get all tests from Login and Maintenance class
login = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
maintenance = unittest.TestLoader().loadTestsFromTestCase(MaintenanceTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([login, maintenance])

# run the suite
#unittest.TextTestRunner(verbosity=2).run(test_suite)


runner = HtmlTestRunner.HTMLTestRunner(output="C:/_D/python-misc/Selenium_Samples/Selenium_POM_Python/Reports")
runner.run(test_suite)



# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())

