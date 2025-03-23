import pytest
from curl import main_site
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import AuthGenerator

auth_generator = AuthGenerator()


@pytest.mark.usefixtures("driver")
class TestLoginService:
    def test_login_via_main_page(self, driver):
        driver.get(main_site)
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.BTN_LOGIN)
        )
        driver.find_element(*Locators.BTN_LOGIN).click()

        email = auth_generator.email_register
        password = auth_generator.password_register

        driver.find_element(*Locators.NAME).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Locators.BTN_ENTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(main_site)
        )

        assert driver.current_url == main_site

    def test_login_via_profile_button(self, driver):
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

        assert driver.current_url == main_site
