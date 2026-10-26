import allure

from helpers.auth_helper import AuthHelper
from locators import login_page_locators

@allure.feature("Проверяем функционал личного кабинета пользователя")
class TestAccountProfileNavigationAndLogout:

    @allure.title(
        "Переход в Личный кабинет авторизованного пользователя по клику на 'Личный кабинет'"
    )
    def test_authorized_user_navigates_to_profile_page(
            self, driver, register_user, account_page, header_page, login_page, registered_user_credentials
    ):

        email, password = registered_user_credentials

        with allure.step(
            "Авторизация пользователя через форму входа и "
            "подтверждение статуса по кнопке 'Оформить заказ'"
        ):
            AuthHelper.login_user_ui(driver, email, password)


        with allure.step("Переход в Личный кабинет через кнопку в интерфейсе"):
            header_page.click_to_personal_account_btn()

        with (allure.step("Проверка наличия элементов профиля")):
            assert account_page.profile_section_is_present( ), \
            "Кнопка 'Профиль' не найдена"

    @allure.title("Проверяем переход из 'Личного кабинета' в раздел 'История заказов'")
    def test_authorized_user_navigates_to_order_history_and_verifies_container(
            self, driver, register_user, account_page, header_page, login_page, registered_user_credentials
    ):
        email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step("Переход в Личный кабинет через кнопку в шапке"):
            header_page.click_to_personal_account_btn()

        with allure.step("Переход в раздел 'История заказов'"):
            account_page.click_order_history_btn()

        with allure.step("Проверяем,что контейнер 'История заказов' отображается в DOM"):
            assert account_page.is_order_history_container_present(), (
                "Контейнер истории заказов не найден"
            )

    @allure.title("Выход из аккаунта и проверка отображения формы входа")
    def test_authorized_user_profile_and_logout(
            self, driver, register_user, account_page, header_page, login_page, registered_user_credentials
    ):
        email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step("Переход в Личный кабинет через кнопку в шапке"):
            header_page.click_to_personal_account_btn()

        with allure.step("Выход из аккаунта"):
            account_page.click_logout_btn()

        with allure.step("Проверяем, что поле Email отображается"):
            assert login_page.is_email_field_visible(), "Поле email не отображается"

        with allure.step("Проверяем, что поле Password отображается"):
            assert login_page.is_password_field_visible(), "Поле password не отображается"

        with allure.step("Проверяем, что кнопка 'Войти' отображается"):
            assert login_page.is_login_btn_visible(), "Кнопка 'Войти' не отображается"