from selenium.webdriver.common.by import By

PROFILE_BTN = (By.XPATH, '//a[@href="/account/profile" and contains(text(), "Профиль")]')
ORDER_HISTORY_BTN = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')
LOGOUT_BTN = (By.XPATH, '//button[normalize-space() = "Выход"]')

NAME_FIELD = (By.CSS_SELECTOR, '.Profile_profileList__3vTor input[name="Name"]')
LOGIN_FIELD = (By.CSS_SELECTOR, '.Profile_profileList__3vTor input[name="name"]')

ORDER_HISTORY_CONTAINER = (By.CSS_SELECTOR, "[class*='OrderHistory_orderHistory']")
ORDERS_LIST = (By.CSS_SELECTOR, "ul[class^='OrderHistory_profileList']")

FIRST_ORDER_ITEM_IN_HISTORY = (By.CSS_SELECTOR, "ul[class^='OrderHistory_'] li:first-child")
FIRST_ORDER_ITEM_NUMBER_IN_HISTORY = (By.CSS_SELECTOR, "p.text_type_digits-default")

