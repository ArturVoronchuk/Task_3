import urls
from locators import login_page_locators, common_locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(BasePage):

    def go_to_login_page_url(self):
        self.driver.get(urls.LOGIN_PAGE_URL)
        return self

    def click_recovery_password_btn(self):
        element = self._wait().until(
            ec.visibility_of_element_located(login_page_locators.RECOVERY_PASSWORD_BTN)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def is_email_field_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_EMAIL_FIELD)

    def is_password_field_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_PASSWORD_FIELD)

    def is_login_btn_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_BTN)