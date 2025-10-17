import time
import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("bind_driver_and_data")
class TestVerifyTooltip:

  @pytest.mark.order(2)
  def test_verify_tooltip(self):
    home_page = HomePage(self.driver)

    if not home_page.logged_in():
      login_page = home_page.click_signin_btn()
      login_page.perform_login(email = self.user_data["email"], password=self.user_data["password"])

    time.sleep(5)
    search_tooltip = home_page.get_tooltip_text_hover(home_page.SEARCH_BAR, home_page.searchbar_tooltip_locator)
    assert search_tooltip != "", "Search bar tooltip is missing"
    print(f"Search tooltip: {search_tooltip}")

    pogimeter_tooltip = home_page.get_tooltip_text_hover(home_page.POGI_METER, home_page.pogimeter_tooltip_locator)
    assert pogimeter_tooltip != "", "Pogimeter tooltip is missing"
    print(f"Pogimeter tooltip: {pogimeter_tooltip}")

    gemcounter_tooltip = home_page.get_tooltip_text_hover(home_page.GEM_COUNTER, home_page.gemcounter_tooltip_locator)
    assert gemcounter_tooltip != "", "Gemcounter tooltip is missing"
    print(f"Gemcounter tooltip: {gemcounter_tooltip}")

    inboxicon_tooltip = home_page.get_tooltip_text_hover(home_page.INBOX_ICON, home_page.inboxicon_tooltip_locator)
    assert inboxicon_tooltip != "", "Inbox icon tooltip is missing"
    print(f"Inbox icon tooltip: {inboxicon_tooltip}")

    friendsicon_tooltip = home_page.get_tooltip_text_hover(home_page.FRIENDS_ICON, home_page.friendsicon_tooltip_locator)
    assert friendsicon_tooltip != "", "Friends icon tooltip is missing"
    print(f"Friends icon tooltip: {friendsicon_tooltip}")

    