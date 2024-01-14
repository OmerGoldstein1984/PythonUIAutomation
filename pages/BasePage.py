from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def enterText(self, locator, textValue):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(textValue)

    # get text from element
    def getText(self, locator):
        return self.driver.find_element(*locator).text

    # check if element is displayed to the user
    def isElementDisplayed(self, locator):
        try:
            self.driver.find_element(*locator).is_displayed()
            return True
        except NoSuchElementException:
            return False

    # wait for element to be part of DOM
    def waitForElement(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
