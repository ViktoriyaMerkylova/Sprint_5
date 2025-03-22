from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации
    # Кнопка личный кабинет
    PROFILE_LINK = [By.XPATH, "//a[@href='/account']"]
    #Кнопка зарегистрироваться
    REGISTER_LINK = [By.XPATH, "//a[@href='/register']"]
    #кнопка имя
    NAME = (By.NAME, 'name')
    # EMAIL
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # пароль
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    #Зарегистрироваться
    REGISTER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"