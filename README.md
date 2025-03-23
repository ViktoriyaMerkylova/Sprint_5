# Sprint 5: UI-тестирование Stellar Burgers


О проекте:

Практикум по UI-тестированию, направленный на тестирование веб-приложения Stellar Burgers.



# Тесты регистрации
class TestSuccessfulRegistration
    
Файл: test_registration.py
    
    
    test_successful_registration 
    #Проверка успешной регистрации

    test_invalid_password_error_message
    #Проверка некорректного пароля при регистрации


# Тесты авторизации
class TestLoginService
   
Файл: test_enty.py
    
    
    test_login_via_main_page
    #Проверка входа 'Войти в аккаунт' на главной

    test_login_via_profile_button
    #Проверка входа через кнопку 'Личный кабинет'

    test_login_via_registration_form_button
    Проверка входа через кнопку в форме регистрации

    test_login_via_forgot_password_form
    #Проверка входа через кнопку в форме восстановления пароля


# Тесты навигации в личныом кабинете
class TestNavigationTo

Файл: test_navigation_to_personal_cabinet.py

    
    test_click_to_login_page_redirect
    #Проверка перехода по клику на 'Личный кабинет'

# Тесты навигации из личного кабинета
class TestNavigationFrom

Файл: test_navigation_from_personal_to_constructor.py
 
    
    def test_click_to_login_page_redirect(self):
    #Проверка перехода по клику на 'Конструктор'

    def test_logo_click_redirect(self):
    #Проверка перехода по клику на логотип Stellar Burgers

# Тесты выхода из аккаунта
class TestLogoutTest:

Файл: test_account_logout.py

    
    test_logout_button_exit_functionality
    Проверка выхода по кнопке 'Выйти' в личном кабинете


# Тесты конструктора
class TestConstructor:

Файл: test_constructor_section.py
    
    
    test_bulki_section_visibility(
     #Проверка перехода к разделу 'Булки'

    test_sauce_section_visibility(self):
    #Проверка перехода к разделу 'Соусы'

    test_filling_section_visibility(self):
    #Проверка перехода к разделу 'Начинки'
