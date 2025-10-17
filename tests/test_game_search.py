import time
import pytest
from pages.home_page import HomePage
from pages.home_page import LoginPage

@pytest.mark.usefixtures("bind_driver_and_data")
class TestGameSearch:

  @pytest.mark.order(3)
  def test_game_search(self):
    
    home_page = HomePage(self.driver)

    if not home_page.logged_in():
      login_page = home_page.click_signin_btn()
      login_page.perform_login(email = self.user_data["email"], password=self.user_data["password"])

    search_page = home_page.search_text(search_text = self.user_data["game_name"])

    assert search_page.are_games_displayed(), "Games are not displayed after search"
    print("Games are displayed after search")

    search_page.click_first_game()

    assert search_page.verify_playnow_btn_present(), "Play now button is not displayed"
    print("Play Now button is visible")
    time.sleep(5)