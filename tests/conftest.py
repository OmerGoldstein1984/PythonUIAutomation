import sys
from sys import platform
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from utils.utils import utils


def pytest_addoption(parser):
    parser.addoption("--browsername", action="store", default="ch", help="ch|ff")
    parser.addoption("--env", action="store", default="test", help="test|production")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed:
        try:
            allure.attach(item.parent.name + '/' + item.name,
                          allure.attach(
                              driver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=allure.attachment_type.PNG)
                          )
        except Exception as e:
            print(f"Failed to attach screenshot: {e}")


def isTestsRunningOnLinux():
    if not sys.platform.startswith('win'):
        return True
    return False


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    firefoxoptions = webdriver.FirefoxOptions()
    chromeoptions = webdriver.ChromeOptions()
    firefoxoptions.add_argument("--headless")
    chromeoptions.add_argument("--headless")
    browsername = request.config.getoption("--browsername")
    env = request.config.getoption("--env")
    site_url = utils.read_config(env, "url")

    if isTestsRunningOnLinux() is True:
        if browsername == "ch":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeoptions)
        elif browsername == "ff":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefoxoptions)

    if isTestsRunningOnLinux() is False:
        if browsername == "ch":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browsername == "ff":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(site_url)
    request.cls.env=env
    request.cls.driver = driver
    yield
    driver.quit()
