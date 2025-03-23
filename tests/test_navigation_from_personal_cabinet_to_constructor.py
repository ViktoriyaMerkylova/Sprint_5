import pytest
from curl import main_site, main_profile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import AuthGenerator

auth_generator = AuthGenerator()


@pytest.mark.usefixtures("driver")
class TestLoginService:
    def test_click_to_login_page_redirect (self, driver):
        driver.get(main_site)
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.PROFILE_LINK)
        )
        driver.find_element(*Locators.PROFILE_LINK).click()

        email = auth_generator.email_register
        password = auth_generator.password_register

        driver.find_element(*Locators.NAME).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.BTN_ENTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site)
        )
        driver.find_element(*Locators.PROFILE_LINK).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_profile)
        )

