from locators import header_page_locators
from pages.base_page import BasePage

class HeaderPage(BasePage):

    def click_to_personal_account_btn(self):
        self.js_click(header_page_locators.PERSONAL_ACCOUNT_BTN)
        return self

    def click_to_constructor_btn(self):
        self.js_click(header_page_locators.CONSTRUCTOR_BTN)
        return self

    def click_to_orders_feed_btn(self):
        self.js_click(header_page_locators.ORDER_FEED_BTN)
        return self
