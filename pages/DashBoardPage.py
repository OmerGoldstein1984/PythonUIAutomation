from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class DashBoardPage(BasePage):
    DASHBOARD_CAPTION = (By.XPATH,"//h6[text()='Dashboard']")
    USERNAME_CLASS = (By.CLASS_NAME,"oxd-userdropdown-name")
    LOGOUT_TEXT_SELECTOR = (By.PARTIAL_LINK_TEXT,"Logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.waitForElement(self.DASHBOARD_CAPTION)

    def getUserName(self):
        return self.getText(self.USERNAME_CLASS)

    def logout(self):
        self.click(self.USERNAME_CLASS)
        self.waitForElement(self.LOGOUT_TEXT_SELECTOR)
        self.click(self.LOGOUT_TEXT_SELECTOR)


