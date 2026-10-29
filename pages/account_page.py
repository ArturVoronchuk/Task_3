from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from locators import account_page_locators, common_locators


class AccountPage(BasePage):

    def click_order_history_btn(self):
        self.js_click(account_page_locators.ORDER_HISTORY_BTN)
        return self

    def wait_for_order_history_container(self, timeout=None):
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)

        wait = self._wait(timeout)
        wait.until(ec.visibility_of_element_located(account_page_locators.ORDER_HISTORY_CONTAINER))

    def is_order_history_container_present(self, timeout=60) -> bool:
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)
        try:
            self._wait(timeout).until(
                ec.presence_of_element_located(account_page_locators.ORDER_HISTORY_CONTAINER)
            )
            return True
        except TimeoutException:
            return False

    def get_name(self):
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR)
        element = self.find_visible_element(account_page_locators.NAME_FIELD)
        return element.get_attribute("value") or ""

    def get_login(self):
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR)
        element = self.find_visible_element(account_page_locators.LOGIN_FIELD)
        return element.get_attribute("value") or ""

    def click_logout_btn(self):
        self.js_click(account_page_locators.LOGOUT_BTN)
        return self

    def wait_and_get_first_order_number(self):

        self._wait().until(ec.visibility_of_element_located(account_page_locators.ORDERS_LIST))

        first_item = self._wait().until(ec.element_to_be_clickable(account_page_locators.FIRST_ORDER_ITEM_IN_HISTORY))

        number_el = first_item.find_element(*account_page_locators.FIRST_ORDER_ITEM_NUMBER_IN_HISTORY)
        return number_el.text.strip()

    def profile_section_is_present(self):
        return self.is_element_present(account_page_locators.PROFILE_BTN)