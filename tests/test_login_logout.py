import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("bind_driver_and_data")
class TestLoginLogout:

  @pytest.mark.order(4)
  def test_login_logout(self):
    home_page = HomePage(self.driver)
    
    # login_page = home_page.click_signin_btn()
    # login_page.perform_login(email = self.user_data["email"], password=self.user_data["password"])

    if home_page.logged_in():
      home_page.perform_logout()

    login_page = home_page.click_signin_btn()

    login_page.perform_login(email = self.user_data["email"], password=self.user_data["password"])

    profile_icon = home_page.get_profile()
    assert profile_icon.is_displayed()

    home_page.perform_logout()
