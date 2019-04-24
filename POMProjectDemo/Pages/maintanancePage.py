from POMProjectDemo.Locators.locators import Locators

class MaintenancePage():

    def __init__(self, driver):
        self.driver = driver

        self.confirm_password_textbox_id = Locators.confirm_password_textbox_id
        self.submit_button_xpath = Locators.submit_button_xpath

    def enter_password(self, password):
        self.driver.find_element_by_id(self.confirm_password_textbox_id).clear()
        self.driver.find_element_by_id(self.confirm_password_textbox_id).send_keys(password)

    def click_verify(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()