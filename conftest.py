import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown(request):
    config = configparser.ConfigParser()
    config.read('configs/config.ini')

    browser = config.get('WEB', 'browser').lower()
    base_url = config.get('WEB', 'base_url')

    # Setup Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    driver.get(base_url)

    # Read user data
    user_data = {
        "country": config.get('USER', 'country'),
        "dob_month": config.get('USER', 'dob_month'),
        "dob_day": config.get('USER', 'dob_day'),
        "dob_year": config.get('USER', 'dob_year'),
        "email": config.get('USER', 'email'),
        "username": config.get('USER', 'username'),
        "password": config.get('USER', 'password'),
        "game_name": config.get('GAME', 'name')
    }

    # Store in request config so it's accessible across all classes
    request.session.driver = driver
    request.session.user_data = user_data

    yield

    driver.quit()


# This ensures every test class gets access to self.driver and self.user_data
@pytest.fixture(scope="class", autouse=True)
def bind_driver_and_data(request):
    request.cls.driver = request.session.driver
    request.cls.user_data = request.session.user_data
