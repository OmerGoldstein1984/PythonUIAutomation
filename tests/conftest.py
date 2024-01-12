import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import allure
import pytest
from selenium import webdriver


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


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver = driver
    yield
    driver.quit()
