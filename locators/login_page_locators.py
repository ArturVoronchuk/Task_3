from selenium.webdriver.common.by import By

LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="text"][name="name"]')
LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"][name="Пароль"]')
LOGIN_BTN = (By.CSS_SELECTOR, 'button.button_button_type_primary__1O7Bx')
RECOVERY_PASSWORD_BTN = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
