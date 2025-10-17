import time
import pytest
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage

@pytest.mark.usefixtures("bind_driver_and_data")
class TestRegistration:
  
    @pytest.mark.order(1)
    def test_user_registration_successfully(self):

        home_page = HomePage(self.driver)

        reg_page = home_page.click_register_free()

        #Verify the page title is correct
        page_title = reg_page.get_page_title()
        assert page_title == "Create account", f"Expected title 'Create account', but got '{page_title}'"

        #Fill Country and DOB form using userdata in conftest
        reg_page.select_country(country = self.user_data["country"])
        reg_page.set_dob(month=self.user_data["dob_month"], day=self.user_data["dob_day"], year=self.user_data["dob_year"])
        reg_page.click_next()

        #Fill email, username and password field using userdata
        reg_page.fill_registration_form(
            email=self.user_data["email"],
            username=self.user_data["username"],
            password=self.user_data["password"]
        )

        #Wait 20 seconds to solve CAPTCHA
        print("Waiting 20 seconds for CAPTCHA...")
        time.sleep(20)

        #Click Next Button
        reg_page.click_next()

        reg_page.check_all_checkboxes()

        reg_page.click_create_account()

        #Wait 20 seconds to enter Validation Code from Email
        print("Waiting 20 seconds for Validation Code...")
        time.sleep(20)
        
        reg_page.click_next()
        
        reg_page.set_screenname(screenname=self.user_data["username"])
        
        reg_page.start_playing()
        # Back to Homepage
        home_page.close_offers()

        profile_icon = home_page.get_profile()
        assert profile_icon.is_displayed()

        time.sleep(5)
