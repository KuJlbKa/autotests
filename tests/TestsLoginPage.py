import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages import LoginPage
from pages import Defaults


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(Defaults.url)
        self.driver.implicitly_wait(10)

    # login to system with valid credentials
    def test_login_with_valid_data(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(0)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_xpath("//*[@id='app-container']/div/div/nav").is_displayed()

    # login to system with incorrect password
    def test_login_with_incorrect_password(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(0)
        home.set_password(1)
        home.sign_in()
        assert self.driver.find_element_by_class_name("text-help").is_displayed()

    # login to system with empty email
    def test_login_with_empty_email(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(1)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]").is_displayed()

    # login to system where email without domain for example test@test
    def test_login_where_email_without_domain(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(2)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_class_name("text-help").is_displayed()

    # login to system where email without first part for example @test.com
    def test_login_where_email_without_first_part(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(5)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]").is_displayed()

    # login to system where email without second part for example test@.com
    def test_login_where_email_without_secont_part(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(6)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]").is_displayed()

    # login to system where email without second part for example test123.com
    def test_login_where_email_without_at(self):
        home = LoginPage.LoginPage(self.driver)
        home.set_login(8)
        home.set_password(0)
        home.sign_in()
        assert self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]").is_displayed()

    # check link forgot password
    def test_link_forgot_password(self):
        home = LoginPage.LoginPage(self.driver)
        home.forgot_password()
        assert "Forgot Password" in self.driver.page_source
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
