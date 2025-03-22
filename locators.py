from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    PROFILE_LINK = [By.XPATH, "//a[@href='/account']"]
    REGISTER_LINK = [By.XPATH, "//a[//a[@href='/register']"]
    NAME = (By.ID, 'Имя')
    EMAIL = (By.ID, 'Email')
    PASSWORD = (By.ID, 'Пароль')
    REGISTER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"