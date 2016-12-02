import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages import Defaults


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def sign_in(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[2]/button").submit()
        self.driver.implicitly_wait(10)

    def forgot_password(self):
        self.driver.find_element_by_css_selector("a.btn").click()


    def set_login(self,item):
        element = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]/input")
        element.clear()
        element.send_keys(Defaults.login[item])

    def set_password(self, item):
        element = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[2]/input")
        element.clear()
        element.send_keys(Defaults.password[item])

    def login(self, login_value, password_value):
        login = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[1]/input")
        login.clear()
        login.send_keys(Defaults.login[login_value])
        password = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[1]/div[2]/input")
        password.clear()
        password.send_keys(Defaults.password[password_value])
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/form/fieldset/div[2]/button").submit()
        self.driver.implicitly_wait(10)

