from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def should_be_login_page(self):
        assert "login" in self.browser.current_url, "Login url is not presented" 
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
