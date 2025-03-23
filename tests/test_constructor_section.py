import pytest
from curl import main_site
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver")
class TestConstructor:
    def test_bulki_section_visibility (self, driver):
        driver.get(main_site)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCE)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.BULKI)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.BULKI_SECTION_TITLE)
        )

        assert driver.find_element(*Locators.BULKI_SECTION_TITLE).is_displayed()

    def test_sauce_section_visibility (self, driver):
        driver.get(main_site)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCE)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.SAUCE_SECTION_TITLE)
        )

        assert driver.find_element(*Locators.SAUCE_SECTION_TITLE).is_displayed()

    def test_filling_section_visibility (self, driver):
        driver.get(main_site)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FILLING)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.FILLING_SECTION_TITLE)
        )

        assert driver.find_element(*Locators.FILLING_SECTION_TITLE).is_displayed()

