import urls
from locators import login_page_locators, common_locators
from pages.base_page import BasePage

class LoginPage(BasePage):

    def go_to_login_page_url(self):
        self.go_to_url(urls.LOGIN_PAGE_URL)
        return self

    def click_recovery_password_btn(self):
        self.js_click(login_page_locators.RECOVERY_PASSWORD_BTN)
        return self

    def is_email_field_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_EMAIL_FIELD)

    def is_password_field_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_PASSWORD_FIELD)

    def is_login_btn_visible(self):
        return self.is_element_present(login_page_locators.LOGIN_BTN)