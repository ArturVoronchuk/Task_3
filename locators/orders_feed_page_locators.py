from selenium.webdriver.common.by import By

FIRST_ORDER_LINK = (By.CSS_SELECTOR, "a[class^='OrderHistory_link']")
MODAL_CONTAINER = (By.CSS_SELECTOR, "div[class*='Modal_modal__container']")
MODAL_HEADER_COMPOSITION_TEXT = (By.XPATH, "//p[contains(text(), 'Cостав')]")

ORDERS_FEED_HEADER = (By.XPATH, '//h1[normalize-space() = "Лента заказов"]')

FEED_ORDER_NUMBER = (By.CSS_SELECTOR, "p.text_type_digits-default")

MODAL_CROSS_BTN = (
    By.CSS_SELECTOR,
    "div[class*='Modal_modal__container'] button[class*='Modal_modal__close']"
)

ALL_TIME_ORDERS_COUNTER = (
    By.XPATH,
    "//p[normalize-space()='Выполнено за все время:']/following-sibling::p[1]"
)

TODAY_ORDERS_COUNTER = (
    By.XPATH,
    "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p[1]"
)

ORDERS_IN_PROGRESS_LIST = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady']")

ORDERS_IN_PROGRESS_ITEM = (By.CSS_SELECTOR, "li.text_type_digits-default")
FEED_ORDER_ITEMS = (By.CSS_SELECTOR, ".OrderHistory_listItem__2x95r")
