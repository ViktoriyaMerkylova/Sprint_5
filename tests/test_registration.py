from selenium.webdriver.common.by import By
import pytest
from curl import main_site,main_login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators
from data import AuthGenerator


@pytest.mark.usefixtures("driver")
class TestSuccessfulRegistration:
    def test_successful_registration(self,driver):
            driver.get(main_site)
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(Locators.PROFILE_LINK)
            )
            driver.find_element(*Locators.PROFILE_LINK).click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(Locators.REGISTER_LINK)
            )
            driver.find_element(*Locators.REGISTER_LINK).click()
            generator = AuthGenerator()
            email = generator.generate_email(number=17, domain="test.com")
            password = generator.generate_password(length=12)

            driver.find_element(*Locators.NAME).send_keys("Viktoriya Merkylova")
            driver.find_element(*Locators.EMAIL).send_keys(email)
            driver.find_element(*Locators.PASSWORD).send_keys(password)

            driver.find_element(*Locators.REGISTER_BUTTON).click()

            WebDriverWait(driver, 10).until(
                EC.url_to_be(main_login)
            )

            assert driver.current_url == main_login
