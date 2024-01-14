import allure
import pytest
from pages.LoginPage import LoginPage
from utils.utils import utils


@pytest.mark.usefixtures("setup")
@allure.feature("login page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story("login page")
class Testlogin:

    @allure.description("This test is to test the login page valid credentials")
    def test_valid_login(self):
        user = utils.read_config(self.env, 'user')
        password = utils.read_config(self.env, 'password')
        login = LoginPage(self.driver)
        login.enterCredentials(user, password)
        assert login.isError() is False

    @allure.description("This test is to test the login page invalid credentials")
    def test_invalid_login(self):
        user = utils.read_config(self.env, 'user')
        login = LoginPage(self.driver)
        login.enterCredentials(user + "123", "123")
        assert login.isError() is True

    @allure.description("This test is to test the dashboard page contains the right user name")
    def test_invalid_user_displayed(self):
        user = utils.read_config(self.env, 'user')
        password = utils.read_config(self.env, 'password')
        login = LoginPage(self.driver)
        login.enterCredentials(user, password)
        dashboard = login.goToDashboard()
        assert dashboard.getUserName() == "Admin"

    @allure.description("This test is login and logout function")
    def test_login_logout(self):
        user = utils.read_config(self.env, 'user')
        password = utils.read_config(self.env, 'password')
        login = LoginPage(self.driver)
        login.enterCredentials(user, password)
        dashboard = login.goToDashboard()
        dashboard.logout()
        assert login.isLoginButtonDisplayed() is True
