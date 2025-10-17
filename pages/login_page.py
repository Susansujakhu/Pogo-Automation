from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, "password")
    NEXT_BUTTON = (By.XPATH, "//a[text()='NEXT']")
    LOGIN_BTN = (By.XPATH, "//a[text()='Sign in']")

    def input_email(self, email):
        self.do_send_keys(self.EMAIL_INPUT, email)

    def click_next(self):
        self.do_click(self.NEXT_BUTTON)

    def input_password(self, password):
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def click_signin(self):
        self.do_click(self.LOGIN_BTN)

    def perform_login(self, email, password):
      self.input_email(email)
      self.click_next()
      self.input_password(password)
      self.click_signin()
