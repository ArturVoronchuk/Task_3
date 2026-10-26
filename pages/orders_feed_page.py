from selenium.common.exceptions import TimeoutException

import urls
from locators import orders_feed_page_locators, common_locators
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage

class OrdersFeedPage(BasePage):

    def wait_orders_feed_page_ready(self, timeout=None):
        if common_locators.OVERLAY_LOCATOR is not None:
            self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)
        return self

    def click_to_first_order_in_feed(self):
        self.wait_orders_feed_page_ready()
        self.click_to_element(orders_feed_page_locators.FIRST_ORDER_LINK)
        return self


    def click_to_order_in_history(self):
        element = self._wait().until(
            ec.visibility_of_element_located(orders_feed_page_locators.FIRST_ORDER_LINK)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def is_modal_appeared_in_dom(self):
        try:
            self._wait().until(ec.presence_of_element_located(orders_feed_page_locators.MODAL_CONTAINER))
            return True
        except TimeoutException:
            return False

    def is_modal_displayed(self):
        try:
            self._wait().until(ec.visibility_of_element_located(orders_feed_page_locators.MODAL_HEADER_COMPOSITION_TEXT))
            return True
        except TimeoutException:
            return False

    def find_order_in_feed_by_number(self, target_number: str):
        items = self._wait().until(ec.presence_of_all_elements_located(orders_feed_page_locators.FEED_ORDER_ITEMS))

        for item in items:
            try:
                num_el = item.find_element(*orders_feed_page_locators.FEED_ORDER_NUMBER)
                if num_el.text.strip() == target_number:
                    self.scroll_into_view(item)
                    return item
            except Exception:
                continue

        raise TimeoutException(f"Order with number '{target_number}' not found in feed.")

    def click_to_modal_window_cross(self, timeout=15):
        cross = self._wait(timeout).until(
            ec.element_to_be_clickable(orders_feed_page_locators.MODAL_CROSS_BTN)
        )
        self._wait(timeout).until(
            lambda d: d.execute_script(
                "const el = arguments[0];"
                "const r = el.getBoundingClientRect();"
                "const top = document.elementFromPoint(r.left + r.width/2, r.top + r.height/2);"
                "return el === top || el.contains(top);",
                cross
            )
        )
        cross.click()
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)
        return self

    def get_total_orders_all_time(self):
        text = self.find_visible_element(
            orders_feed_page_locators.ALL_TIME_ORDERS_COUNTER
        ).text.strip()
        return int(text)

    def get_total_orders_today(self):
        text = self.find_visible_element(
            orders_feed_page_locators.TODAY_ORDERS_COUNTER
        ).text.strip()
        return int(text)

    def go_to_constructor_url(self):
        self.driver.get(urls.MAIN_PAGE_URL)
        return self

    def get_order_numbers_in_progress_section(self) -> list[int]:
        ul = self.find_visible_element(
            orders_feed_page_locators.ORDERS_IN_PROGRESS_LIST
        )
        lis = ul.find_elements(*orders_feed_page_locators.ORDERS_IN_PROGRESS_ITEM)
        return [int(li.text.strip()) for li in lis]

    def wait_order_in_progress_section(self, order_number: int, timeout=15):
        self._wait(timeout).until(
            lambda d: order_number in self.get_order_numbers_in_progress_section()
        )
        return self

    def is_orders_feed_header_visible(self, timeout=10):
        return self.is_element_present(
            orders_feed_page_locators.ORDERS_FEED_HEADER, timeout
        )