from selenium.webdriver.common.by import By
from pages.base_page import BasePage

"""
Page Object for the User Registration page.
"""
class RegistrationPage(BasePage):

    # --- Locators ---
    COUNTRY_DROPDOWN = (By.NAME, "country")
    MONTH_DROPDOWN = (By.NAME, "dobMonth")
    DAY_DROPDOWN = (By.NAME, "dobDay")
    YEAR_DROPDOWN = (By.NAME, "dobYear")
    EMAIL_INPUT = (By.ID, 'email')
    EA_ID_INPUT = (By.ID, 'originId')
    PASSWORD_INPUT = (By.ID, "password")
    SCREENNAME = (By.ID, "screenname")

    CHECKBOX_EMAIL_VISIBILITY = (By.ID, "email-visibility-container")
    CHECKBOX_CONTACT_ME = (By.ID, "contact-me-container")
    CHECKBOX_READ_ACCEPT = (By.ID, "read-accept-container")

    NEXT_BUTTON = (By.XPATH, "//a[text()='Next']")
    CREATE_ACCOUNT_BUTTON = (By.ID, "submitBtn")

    # --- Initializer ---
    def __init__(self, driver):
        super().__init__(driver)

    def select_country(self, country):
      self.select_dropdown_by_visible_text(self.COUNTRY_DROPDOWN, country)

    def set_dob(self, month, day, year):
      self.select_dropdown_by_visible_text(self.MONTH_DROPDOWN, month)
      self.select_dropdown_by_visible_text(self.DAY_DROPDOWN, day)
      self.select_dropdown_by_visible_text(self.YEAR_DROPDOWN, year)

    def click_next(self):
        self.do_click(self.NEXT_BUTTON)

    def fill_registration_form(self, email, username, password):
        self.do_send_keys(self.EMAIL_INPUT, email)
        self.do_send_keys(self.EA_ID_INPUT, username)
        self.do_send_keys(self.PASSWORD_INPUT, password)

    def check_all_checkboxes(self):
        self.check_checkbox(self.CHECKBOX_EMAIL_VISIBILITY)
        self.check_checkbox(self.CHECKBOX_CONTACT_ME)
        self.check_checkbox(self.CHECKBOX_READ_ACCEPT)

    def click_create_account(self):
        self.do_click(self.CREATE_ACCOUNT_BUTTON)

    def set_screenname(self, screenname):
        if not self.check_value_exists(self.SCREENNAME):
          self.do_send_keys(self.SCREENNAME, screenname)
        self.do_click(self.get_button_by_text("Next"))

    def start_playing(self):
        self.do_click(self.get_button_by_text("Start Playing On Pogo"))

    def get_page_title(self):
        """
        Waits for the page title to be "Register" and returns it.
        This can be used for an assertion in the test.
        """
        if self.get_title("Create account"):
             return self.driver.title
        return None