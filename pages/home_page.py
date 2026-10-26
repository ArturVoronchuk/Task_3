import urls
from locators import home_page_locators, common_locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class HomePage(BasePage):

    def wait_home_page_ready(self, timeout=None):
        if common_locators.OVERLAY_LOCATOR is not None:
            self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)
        return self

    def go_to_orders_feed_url(self):
        self.go_to_url(urls.ORDERS_FEED_URL)
        return self

    def go_to_login_page_url(self):
        self.go_to_url(urls.LOGIN_PAGE_URL)
        return self

    def click_on_place_order_btn(self):
        self.wait_home_page_ready()
        self.click_to_element(home_page_locators.ORDER_BUTTON)
        return self

    def click_to_ingredient_open(self):
        element = self._wait().until(
            ec.visibility_of_element_located(home_page_locators.INGREDIENT_CARD_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def click_on_cross(self):
        element = self._wait().until(
            ec.visibility_of_element_located(home_page_locators.CROSS_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def add_bun_to_basket(self):
        return self.drag_and_drop_js(
            home_page_locators.INGREDIENT_BUNS,
            home_page_locators.BASKET_SLOT
        )

    def get_new_order_number(self, timeout=5):
        self._wait(timeout).until(
            lambda d: d.find_element(
                *home_page_locators.ORDER_NUMBER_IN_MODAL
            ).text.strip() not in ("", "9999")
        )
        text = self.driver.find_element(
            *home_page_locators.ORDER_NUMBER_IN_MODAL
        ).text.strip()
        return int(text)

    def get_order_status_text(self):
        return self.find_visible_element(
            home_page_locators.ORDER_STATUS
        ).text.strip()

    def is_ingredient_modal_opened(self, timeout=10) -> bool:
        return self.is_element_present(
            home_page_locators.INGREDIENT_MODAL_TITLE, timeout
        )

    def get_ingredient_counter_value(self, timeout=10) -> int:
        counter = self._wait(timeout).until(
            ec.visibility_of_element_located(home_page_locators.INGREDIENT_COUNTER)
        )
        return int(counter.text.strip())