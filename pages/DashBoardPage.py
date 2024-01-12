from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class DashBoardPage(BasePage):
    USERNAME_CLASS = (By.CLASS_NAME,"oxd-userdropdown-name")

    def __init__(self, driver):
        super().__init__(driver)
        self.waitForElement(self.USERNAME_CLASS)

    def getUserName(self):
        return self.getText(self.USERNAME_CLASS)
