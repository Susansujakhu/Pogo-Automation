from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located((locator)))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable((locator)))

    def wait_implicitly(self, time):
        self.driver.implicitly_wait(time)

    def wait_for_elements_presence(self, locator, timer=5):
        try:
            return WebDriverWait(self.driver, timer).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []  # Return empty list if not found

    def select_dropdown_by_value(self, locator, value):
        element = self.wait_for_element(locator)
        Select(element).select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text):
        element = self.wait_for_element(locator)
        Select(element).select_by_visible_text(text)

    def check_checkbox(self, locator):
        try:
          checkbox = self.wait_for_element(locator)
          #Check if it is not already selected
          if not checkbox.is_selected():
              checkbox.click()
        except TimeoutException:
            print(f"Error: Element with locator {locator} was not available after 15 seconds.")
            raise

    def do_click(self, locator):
        try:
            self.wait_for_element_clickable(locator).click()
        except TimeoutException:
            print(f"Error: Element with locator {locator} was not clickable after 15 seconds.")
            raise

    def do_send_keys(self, locator, text):
        try:
            self.wait_for_element(locator).send_keys(text)
        except TimeoutException:
            print(f"Error: Element with locator {locator} was not visible after 10 seconds.")
            raise

    def get_element_text(self, locator):
        try:
            element = self.wait_for_element(locator)
            return element.text
        except TimeoutException:
            print(f"Error: Element with locator {locator} was not visible after 10 seconds.")
            raise

    def get_button_by_text(self, button_text):
      return (By.XPATH, f"//button[div[text()='{button_text}']]")


    def check_value_exists(self, locator):
        element = self.wait_for_element(locator)
        return bool(element.text.strip())

    def press_enter(self, element):
        element.send_keys(Keys.ENTER)

    def get_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return True
        except TimeoutException:
            print(f"Error: Title did not match '{title}' after 10 seconds.")
            return False