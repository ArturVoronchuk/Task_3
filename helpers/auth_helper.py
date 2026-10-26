from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators import common_locators, login_page_locators, home_page_locators

class AuthHelper:
    @staticmethod
    def login_user_ui(driver, email, password):
        wait = WebDriverWait(driver, 15)

        wait.until(ec.invisibility_of_element_located(
            common_locators.OVERLAY_LOCATOR)
        )

        email_field = wait.until(ec.visibility_of_element_located(
            login_page_locators.LOGIN_EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = driver.find_element(
            *login_page_locators.LOGIN_PASSWORD_FIELD
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = driver.find_element(*login_page_locators.LOGIN_BTN)

        driver.execute_script("arguments[0].click();", login_button)

        wait.until(ec.visibility_of_element_located(home_page_locators.ORDER_BUTTON))
