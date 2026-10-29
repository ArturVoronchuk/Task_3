import allure

from locators import forgot_password_locators

@allure.feature("Проверяем функционал восстановления пароля")
class TestForgotPassword:

    @allure.title(
        "Клик по кнопке 'Восстановить пароль' на главной странице"
    )
    def test_navigate_to_recovery_page(self, forgot_password_page, header_page, login_page):

        with allure.step("Клик по кнопке «Восстановить пароль» "):
            login_page.click_recovery_password_btn()

        with allure.step("Проверяем, что на странице восстановления есть поле email"):
            assert forgot_password_page.is_email_field_present(), (
                "Поле ввода email не отображается"
            )

        with allure.step("Проверяем, что на странице восстановления есть кнопка «Восстановить»"):
            assert forgot_password_page.is_submit_recovery_btn_present(), (
                "Кнопка «Восстановить» не отображается"
            )

    @allure.title(
        "Заполнение поля email и нажатие на конопку 'Восстановить' "
        "редиректят на форму заполнения пароля поддтверждения кода"
    )
    def test_email_and_submit_redirects(self, forgot_password_page, login_page):
        email = "test_user@ya.ru"

        with allure.step("Клик по кнопке «Восстановить пароль» "):
            login_page.click_recovery_password_btn()

        with allure.step(f"Вводим '{email}' в поле Email"):
            forgot_password_page.enter_email(email)

        with allure.step("Нажимаем кнопку «Восстановить»"):
            forgot_password_page.click_submit_recovery_btn()

        with allure.step("Ждём исчезновения оверлея после отправки формы"):
            forgot_password_page.wait_overlay_after_submit()

        with allure.step("Проверяем, что появилось поле для ввода нового пароля"):
            assert forgot_password_page.is_new_password_field_present(), (
                "Не появилось поле ввода нового пароля"
            )

        with allure.step("Проверяем, что появилось поле подтверждения кодом"):
            assert forgot_password_page.is_code_from_email_field_present(), (
                "Не появилось поле «Введите код из письма» после отправки формы"
            )

    @allure.title("Клик по иконке показывает пароль (type меняется на text)")
    def test_toggle_password_shows_text(self, forgot_password_page):
        email = "test_user@ya.ru"
        password = "12345"

        with allure.step(f"Вводим email '{email}' для продолжения"):
            forgot_password_page.enter_email(email)

        with allure.step("Нажимаем по кнопке 'Восстановить'"):
            forgot_password_page.click_submit_recovery_btn()

        with allure.step("Вводим новый пароль"):
            forgot_password_page.enter_new_password(password)

        with allure.step("Кликаем по иконке «показать/скрыть пароль» (глаз)"):
            forgot_password_page.click_toggle_password()

        with allure.step("Проверяем, что пароль открылся (type стал 'text')"):
            assert forgot_password_page.is_password_field_type_text(), (
                "Пароль не открылся: атрибут type не изменился на 'text'"
            )