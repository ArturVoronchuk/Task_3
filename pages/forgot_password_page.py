from locators import forgot_password_locators, common_locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class ForgotPasswordPage(BasePage):

    def enter_email(self, email):
        self.send_keys(
            forgot_password_locators.RECOVERY_EMAIL_FIELD,
            email
        )
        return self

    def enter_new_password(self, password):
        self.send_keys(
            forgot_password_locators.NEW_PASSWORD_INPUT_FIELD,
            password
        )
        return self

    def wait_overlay_after_submit(self, timeout=30):
        self.wait_overlay_disappears(common_locators.OVERLAY_LOCATOR, timeout)
        return self

    def click_submit_recovery_btn(self):
        self.js_click(forgot_password_locators.SUBMIT_RECOVERY_BTN)
        return self

    def get_header_text(self):
        self.get_text(*forgot_password_locators.RECOVERY_PAGE_HEADER)
        return self

    def click_toggle_password(self, timeout=10):
        self.js_click(forgot_password_locators.TOGGLE_PASSWORD_ICON)
        return self

    def is_email_field_present(self, timeout=5):
        return self.is_element_present(
            forgot_password_locators.RECOVERY_EMAIL_FIELD, timeout
        )

    def is_submit_recovery_btn_present(self, timeout=5):
        return self.is_element_present(
            forgot_password_locators.SUBMIT_RECOVERY_BTN, timeout
        )

    def is_new_password_field_present(self, timeout=5):
        return self.is_element_present(
            forgot_password_locators.NEW_PASSWORD_INPUT_FIELD, timeout
        )

    def is_code_from_email_field_present(self, timeout=5):
        return self.is_element_present(
            forgot_password_locators.ENTER_CODE_FROM_EMAIL_FIELD, timeout
        )

    def is_password_field_type_text(self, timeout=10):
        element = self._wait(timeout).until(
            ec.presence_of_element_located(
                forgot_password_locators.NEW_PASSWORD_INPUT_FIELD
            )
        )
        return element.get_attribute("type") == "text"