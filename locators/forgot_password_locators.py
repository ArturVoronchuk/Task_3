from selenium.webdriver.common.by import By

RECOVERY_PAGE_HEADER = (By.XPATH, '//h2[contains(text(), "Восстановление пароля")]')
RECOVERY_EMAIL_FIELD = (
    By.XPATH,
    '//label[contains(text(), "Email")]/following-sibling::input[1]'
)
SUBMIT_RECOVERY_BTN = (By.XPATH, '//button[normalize-space()="Восстановить"]')
NEW_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="Введите новый пароль"]')

ENTER_CODE_FROM_EMAIL_FIELD = (
    By.CSS_SELECTOR,
    'fieldset.Auth_fieldset__1QzWN .input__textfield[type="text"]'
)
TOGGLE_PASSWORD_ICON = (By.CSS_SELECTOR, 'div.input__icon.input__icon-action')
