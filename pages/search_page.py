from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
  GAME_WRAPPER = (By.CLASS_NAME, 'gameWrapper__2jNw6')
  PLAY_NOW_BTN = (By.XPATH, "//button[div[text()='Play Now']]")

  def are_games_displayed(self):
    print(len(self.wait_for_elements_presence(self.GAME_WRAPPER, 10)))
    return len(self.wait_for_elements_presence(self.GAME_WRAPPER, 10)) > 0
  
  def click_first_game(self):
    games = self.wait_for_elements_presence(self.GAME_WRAPPER)
    games[0].click()

  def verify_playnow_btn_present(self):
    return len(self.wait_for_elements_presence(self.PLAY_NOW_BTN)) > 0
  