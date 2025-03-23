# Sprint 5: UI-тестирование Stellar Burgers


О проекте:
""
Практикум по UI-тестированию, направленный на тестирование веб-приложения Stellar Burgers.
""


# Тесты регистрации
class TestSuccessfulRegistration:
    """
    Файл: test_registration.py
    """
    
    def test_successful_registration(self):
        """Проверка успешной регистрации"""
        pass

    def test_invalid_password_error_message(self):
        """Проверка некорректного пароля при регистрации"""
        pass


# Тесты авторизации
class TestLoginService:
    """
    Файл: test_enty.py
    """
    
    def test_login_via_main_page(self):
        """Проверка входа 'Войти в аккаунт' на главной"""
        pass

    def test_login_via_profile_button(self):
        """Проверка входа через кнопку 'Личный кабинет'"""
        pass

    def test_login_via_registration_form_button(self):
        """Проверка входа через кнопку в форме регистрации"""
        pass

    def test_login_via_forgot_password_form(self):
        """Проверка входа через кнопку в форме восстановления пароля"""
        pass


# Навигация в личный кабинет
class TestNavigationTo:
    """
    Файл: test_navigation_to_personal_cabinet.py
    """
    
    def test_click_to_login_page_redirect(self):
        """Проверка перехода по клику на 'Личный кабинет'"""
        pass


# Навигация из личного кабинета
class TestNavigationFrom:
    """
    Файл: test_navigation_from_personal_to_constructor.py
    """
    
    def test_click_to_login_page_redirect(self):
        """Проверка перехода по клику на 'Конструктор'"""
        pass

    def test_logo_click_redirect(self):
        """Проверка перехода по клику на логотип Stellar Burgers"""
        pass


# Выход из аккаунта
class TestLogoutTest:
    """
    Файл: test_account_logout.py
    """
    
    def test_logout_button_exit_functionality(self):
        """Проверка выхода по кнопке 'Выйти' в личном кабинете"""
        pass


# Тесты конструктора
class TestConstructor:
    """
    Файл: test_constructor_section.py
    """
    
    def test_bulki_section_visibility(self):
        """Проверка перехода к разделу 'Булки'"""
        pass

    def test_sauce_section_visibility(self):
        """Проверка перехода к разделу 'Соусы'"""
        pass

    def test_filling_section_visibility(self):
        """Проверка перехода к разделу 'Начинки'"""
        pass


# Покрытие функционалом:
# - Регистрация и авторизация пользователей
# - Навигация по сайту
# - Работа с личным кабинетом
# - Функционал конструктора заказов


# Цели тестирования:
# - Проверка корректности работы форм регистрации и авторизации
# - Тестирование навигации между разделами
# - Проверка работы функционала личного кабинета
# - Тестирование работы конструктора заказов


# Рекомендации по использованию:
# - Все тесты организованы по функциональному принципу
# - Каждый тест имеет понятное название, отражающее его назначение
# - Структура тестов позволяет легко добавлять новую функциональность
# - Тесты независимы и могут выполняться как по отдельности, так и в составе всего набора
