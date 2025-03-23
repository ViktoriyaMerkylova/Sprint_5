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
    #Локатор Некоректного пароля
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    #Локаторы по кнопке «Войти в аккаунт» на главной
    #Кнопка «Войти в аккаунт»
    BTN_LOGIN = By.XPATH,"//button[text()='Войти в аккаунт']"
    #Локатор пароля при входе
    PASSWORD_INPUT = (By.NAME, "Пароль")
    #Локатор кнопки Войти
    BTN_ENTER = (By.XPATH, "//button[text()='Войти']")
    #Локатор кнопки Войти через регистрацию
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    #Локатор Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    #Локатор логотипа
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

