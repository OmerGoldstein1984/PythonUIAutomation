import allure
import pytest

from pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup")
@allure.feature("login page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("login page")
class Testlogin:
    @allure.description("This test is to test the login page valid credentials")
    def test_valid_login(self):
        login = LoginPage(self.driver)
        login.enterCredentials("Admin", "admin123")
        assert login.isError() is False

    @allure.description("This test is to test the login page invalid credentials")
    def test_invalid_login(self):
        login = LoginPage(self.driver)
        login.enterCredentials("Admin123", "admin123")
        assert login.isError() is True
    @allure.description("This test is to test the dashboard page contains the right user name")
    def test_invalid_user_displayed(self):
        login = LoginPage(self.driver)
        login.enterCredentials("Admin", "admin123")
        assert login.isError() is False
        dashboard = login.goToDashboard()
        assert dashboard.getUserName() == "Admin"
