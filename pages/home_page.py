from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.search_page import SearchPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
  REGISTER_FREE = (By.XPATH, "//button[.//div[text()='Register free']]")
  SIGNIN_BTN = (By.XPATH, "//button[.//div[text()='Sign In']]")
  PROFILE_ICON = (By.XPATH, "//img[@alt='Avatar Image']")
  SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search games']")
  POGI_METER = (By.CSS_SELECTOR, ".pogiCountWrapper__3TlsE")
  GEM_COUNTER = (By.CSS_SELECTOR, ".gemCountWrapper__btwDb")
  INBOX_ICON = (By.CSS_SELECTOR, ".inboxIcon__2I_U_")
  FRIENDS_ICON = (By.CSS_SELECTOR, ".friendsIcon__1lHFG")

  searchbar_tooltip_locator = (By.CSS_SELECTOR, "div[class*='onboardingTooltip']")
  pogimeter_tooltip_locator = (By.XPATH, "//div[@class='pogiCountWrapper__3TlsE']//div[contains(@class, 'onboardingTooltip')]")
  gemcounter_tooltip_locator = (By.XPATH, "//div[contains(@class, 'gemCountWrapper__btwDb')]//div[contains(@class, 'onboardingTooltip')]")
  inboxicon_tooltip_locator = (By.XPATH, "//div[contains(@class, 'inboxIcon__2I_U_')]//div[contains(@class, 'onboardingTooltip')]")
  friendsicon_tooltip_locator = (By.XPATH, "//div[contains(@class, 'friendsIcon__1lHFG')]//div[contains(@class, 'onboardingTooltip')]")




  def __init__(self, driver):
        super().__init__(driver)

  def click_signin_btn(self):
      self.do_click(self.SIGNIN_BTN)
      return LoginPage(self.driver)

  def click_register_free(self):
      self.do_click(self.REGISTER_FREE)
      return RegistrationPage(self.driver)
  
  def close_offers(self):
      try:
        self.do_click(self.get_button_by_text("Continue"))
      except:
        print("No Popups")

  def get_profile(self):
    return self.wait_for_element(self.PROFILE_ICON)

  def search_text(self, search_text):
     self.do_send_keys(self.SEARCH_BAR, search_text)
     self.press_enter(self.wait_for_element(self.SEARCH_BAR))
     return SearchPage(self.driver)

  def logged_in(self):
     return len(self.wait_for_elements_presence(self.SIGNIN_BTN)) <= 0

  def click_logout_btn(self):
     self.do_click(self.get_button_by_text("Sign Out"))

  def perform_logout(self):
    profile_icon = self.get_profile()
    profile_icon.click()
    self.click_logout_btn()

  def get_tooltip_text_hover(self, locator, tooltip):
      element = self.driver.find_element(*locator)
      ActionChains(self.driver).move_to_element(element).pause(0.5).perform()
      tooltip_el = WebDriverWait(self.driver, 15).until(
          EC.visibility_of_element_located(tooltip)
      )
      return tooltip_el.text.strip()
  
