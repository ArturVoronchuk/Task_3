import allure

from helpers.auth_helper import AuthHelper
from urls import ORDERS_FEED_URL

@allure.feature("Проверяем функционал создания и оформления заказов'")
class TestOrdersFeed:

    @allure.title("Переход по клику ленты заказов отбражает заголовок 'Лента заказов'")
    def test_transition_to_orders_feed_and_verify_order_feed_header(self, header_page, orders_feed_page):

        with allure.step("Переход по клику на 'Лента заказов'"):
            header_page.click_to_orders_feed_btn()

        with allure.step("Проверяем, что URL соответствует ленте заказов"):
            assert orders_feed_page.driver.current_url == ORDERS_FEED_URL, \
                f"Ожидался URL: {ORDERS_FEED_URL}, но открыт: {orders_feed_page.driver.current_url}"

        with allure.step("Проверяем, что заголовок 'Лента заказов' отображается"):
            assert orders_feed_page.is_orders_feed_header_visible(), (
                "Заголовок не отображается. Переход по клику 'Лента заказов' не выполнен"
            )

    @allure.title("Клик по заказу открывает всплывающее окно с деталями заказа")
    def test_clicking_on_order_opens_details_modal_window(
            self, orders_feed_page, registered_user_credentials, header_page, register_user, driver, login_page
    ):
        with allure.step("Создаем пользователя"):
            email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step("Переход по клику на 'Лента заказов'"):
            header_page.click_to_orders_feed_btn()

        with allure.step("Нажимаем на карточку заказа"):
            orders_feed_page.click_to_order_in_history()

        with allure.step("Проверяем, что модальное окно заказа появилось в DOM"):
            assert orders_feed_page.is_modal_appeared_in_dom(), \
            "Модальное окно отстуствует в DOM"

        with allure.step("Проверяем, что модальное окно отобразилось на странице"):
            assert orders_feed_page.is_modal_displayed(), \
            "Модальное окно не отобразилось"

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_users_orders_displayed_in_orders_feed(
            self, orders_feed_page, registered_user_credentials, register_user, driver,
            home_page, header_page, account_page, login_page
    ):

        with allure.step("Создаем пользователя"):
            email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step(
                "Создаем заказ: "
                "Перетаскиваем ингредиент в 'корзину заказов'"
        ):
            home_page.add_bun_to_basket()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            home_page.click_on_place_order_btn()

        with allure.step("Закрываем модальное окно заказа"):
            home_page.click_on_cross()

        with allure.step("Переходим в Личный кабинет"):
            header_page.click_to_personal_account_btn()

        with allure.step("Переходим в Историю заказов"):
            account_page.click_order_history_btn()

        with allure.step("Берем номер первого заказа в списке"):
            order_number = account_page.wait_and_get_first_order_number()

        with allure.step(f"Переходим в «Лента заказов» и ищем заказ с номером {order_number}"):
            header_page.click_to_orders_feed_btn()
            found_card = orders_feed_page.find_order_in_feed_by_number(order_number)

        with allure.step("Проверяем, что заказ из Истории отображается в Ленте"):
            assert found_card.is_displayed(), f"Карточка заказа {order_number} не отображается"

    @allure.title("Счетчик 'Выполнено за всё время увеличивается' увеличивается при создании нового заказа")
    def test_new_order_increments_orders_counters(
            self, orders_feed_page, registered_user_credentials, register_user, driver,
            header_page, home_page, login_page
    ):
        with allure.step("Создаем пользователя"):
            email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step("Переходим по кнопке 'Лента заказов'"):
            header_page.click_to_orders_feed_btn()

        with allure.step("Сохраняем текущее количество заказов за все время"):
            current_number_all_time_orders = orders_feed_page.get_total_orders_all_time()

        with allure.step("Сохраняем текущее количество заказов за сегодня"):
            current_number_today_orders = orders_feed_page.get_total_orders_today()

        with allure.step("Переходим по по клику в 'Конструктор'"):
            header_page.click_to_constructor_btn()

        with allure.step(
                "Создаем заказ: "
                "Перетаскиваем ингредиент в 'корзину заказов'"
        ):
            home_page.add_bun_to_basket()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            home_page.click_on_place_order_btn()

        with allure.step("Закрываем модальное окно заказа"):
            home_page.click_on_cross()

        with allure.step("Переходим в 'Ленту заказов'"):
            header_page.click_to_orders_feed_btn()

        with allure.step(
                "Проверяем, что новое количество заказов за все время стало больше "
                "после создания заказа"
        ):
            assert current_number_all_time_orders < orders_feed_page.get_total_orders_all_time(), (
                "Количество заказов за все время не увеличилось"
            )

        with allure.step(
                "Проверяем, что новое количество заказов за все сегодня стало больше "
                "после создания заказа"
        ):
            assert current_number_today_orders < orders_feed_page.get_total_orders_today(), (
            "Количество заказов за сегодня не увеличилось"
            )

    @allure.title(
        "Проверяем, что после оформления заказа его номер появляется в разделе 'В работе'"
    )
    def test_new_order_number_displayed_in_progress_section(
            self, orders_feed_page, registered_user_credentials, register_user, driver,
            home_page, header_page, login_page
    ):
        with allure.step("Создаем пользователя"):
            email, password = registered_user_credentials

        with allure.step("Авторизация через форму входа"):
            AuthHelper.login_user_ui(driver, email, password)

        with allure.step(
                "Создаем заказ: "
                "Перетаскиваем ингредиент в 'корзину заказов'"
        ):
            home_page.add_bun_to_basket()

        with allure.step("Нажимаем кнопку 'Оформить заказ'"):
            home_page.click_on_place_order_btn()

        with allure.step("Сохраняем номер заказа в переменную"):
            new_order_number = home_page.get_new_order_number()

        with allure.step("Закрываем модальное окно заказа"):
            home_page.click_on_cross()

        with allure.step("Переходим по клику в 'Лента заказов'"):
            header_page.click_to_orders_feed_btn()

        with allure.step("Ждём, что номер нового заказа появляется в секции 'В работе'"):
            orders_feed_page.wait_order_in_progress_section(new_order_number)

        with allure.step("Сохраняем список заказов в статусе 'В работе' в переменную"):
            in_progress = orders_feed_page.get_order_numbers_in_progress_section()

        with allure.step("Проверяем, что номер нового заказа находится в секции 'В работе:'"):
            assert new_order_number in in_progress, (
                "Номер заказа отсутствует среди заказов в статусе 'В работе'"
            )