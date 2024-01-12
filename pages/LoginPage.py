from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.DashBoardPage import DashBoardPage


class LoginPage(BasePage):
    USERNAME_TEXTBOX_NAME = (By.NAME,"username")
    PASSWORD_TEXTBOX_NAME = (By.NAME,"password")
    LOGIN_BUTTON_CLASS = (By.CLASS_NAME,"orangehrm-login-button")
    ERROR_SELECTOR = (By.XPATH,"//p[text()='Invalid credentials']")

    def __init__(self, driver):
        super().__init__(driver)
        self.waitForElement(self.LOGIN_BUTTON_CLASS)

    def enterCredentials(self, username: str, password: str) -> None:
        self.enterText(self.USERNAME_TEXTBOX_NAME, username)
        self.enterText(self.PASSWORD_TEXTBOX_NAME, password)
        self.click(self.LOGIN_BUTTON_CLASS)

    def isError(self):
        try:
            self.waitForElement(self.ERROR_SELECTOR)
            return True
        except:
            return False

    def goToDashboard(self):
        return DashBoardPage(self.driver)
