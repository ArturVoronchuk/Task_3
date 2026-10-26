from locators import header_page_locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class HeaderPage(BasePage):

    def click_to_personal_account_btn(self):
        element = self._wait().until(
            ec.visibility_of_element_located(header_page_locators.PERSONAL_ACCOUNT_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def click_to_constructor_btn(self):
        element = self._wait().until(
            ec.visibility_of_element_located(header_page_locators.CONSTRUCTOR_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def click_to_orders_feed_btn(self):
        element = self._wait().until(
            ec.visibility_of_element_located(header_page_locators.ORDER_FEED_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self
