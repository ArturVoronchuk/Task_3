import allure

from helpers.auth_helper import AuthHelper
from urls import MAIN_PAGE_URL

@allure.feature("Проверяем, основной функционал сайта stellar burgers")
class TestMainFunctionOfHomePage:

    @allure.title("Переход по клику на 'Конструктор' отображает вкладки с составляющими частями бургера:"
                  "Булки, Соусы, Начинки")
    def test_click_constructor_btn_displays_the_ingredients(
            self, header_page, home_page, orders_feed_page
    ):

        with allure.step("Переход по клику на 'Конструктор'"):
            header_page.click_to_constructor_btn()

        with allure.step("Проверяем, что URL соответствует главной странице"):
            assert home_page.get_current_url() == MAIN_PAGE_URL, \
                f"Ожидался URL: {MAIN_PAGE_URL}, но открыт: {home_page.get_current_url()}"

        with allure.step("Проверяем, что вкладка 'Булки' отображается"):
            assert home_page.is_buns_tab_visible(), \
            "Вкладка 'Булки' не отображается"

        with allure.step("Проверяем, что вкладка 'Соусы' отображается"):
            assert home_page.is_sauces_tab_visible(), \
            "Вкладка 'Соусы' не отображается"

        with allure.step("Проверяем, что вкладка 'Начинки' отображается"):
            assert home_page.is_fillings_tab_visible(), \
                "Вкладка 'Начинки' не отображается"

    @allure.title("Клик на ингредиент открывает вслпывающее окно с описанием ингредиента")
    def test_click_on_ingredient_opens_a_card_with_its_description(self, home_page):

        with allure.step("Нажимаем на карточку ингредиента"):
            home_page.click_to_ingredient_open()

        with allure.step("Проверяем, что карточка ингредиента открылась"):
            assert home_page.is_ingredient_modal_opened(), (
                "Карточка ингредиента не открылась"
            )

    @allure.title("Всплывающее окно закрывается при нажатии на крестик")
    def test_click_on_cross_closes_pop_up_modal_window(self, home_page):

        with allure.step("Нажимаем на карточку ингредиента"):
            home_page.click_to_ingredient_open()

        with allure.step("Нажимаем кнопку закрытия карточки ингредиента (крестик)"):
            home_page.click_on_cross()

        with allure.step("Проверяем, что карточка ингредиента закрылась"):
            assert home_page.card_of_ingredient(), \
            "Карточка ингредиента все не закрылась"

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_adding_ingredient_increases_the_counter_by_two(self, home_page):

        with allure.step("Перетаскиваем ингредиент булки в 'корзину заказов'"):
            home_page.add_bun_to_basket()

        with allure.step("Проверяем, что счётчик ингредиента увеличился на 2"):
            counter_value = home_page.get_ingredient_counter_value()
            assert counter_value == 2, (
                f"Счётчик ингредиента не увеличился на 2: {counter_value}"
            )

    @allure.title("Проверяем, что авторизованный пользователь может сделать заказ")
    def test_authorized_user_submits_order_and_verifies_confirmation_modal_content(
            self, home_page, registered_user_credentials, register_user, driver
    ):

        with allure.step("Переходим на страницу авторизации"):
            home_page.go_to_login_page_url()

        with allure.step("Создаем пользователя"):
            email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step("Перетаскиваем ингредиент в 'корзину заказов'"):
            home_page.add_bun_to_basket()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            home_page.click_on_place_order_btn()

        with allure.step("Проверяем, что появилось модальное окно заказа с номером"):
            order_number = home_page.get_new_order_number()
            assert order_number > 0, f"Номер заказа некорректный: {order_number}"

        with allure.step("Проверяем, что статус заказа — «Ваш заказ начали готовить»"):
            order_status = home_page.get_order_status_text()
            assert order_status == "Ваш заказ начали готовить", (
                f"Статус заказа не совпадает: ожидалось 'Ваш заказ начали готовить', "
                f"получено '{order_status}'"
            )
