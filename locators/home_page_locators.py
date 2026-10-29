from selenium.webdriver.common.by import By

INGREDIENT_CARD_BTN = (
    By.CSS_SELECTOR,
    "ul[class*='BurgerIngredients_ingredients__list'] > a"
)

CROSS_BTN = (
    By.CSS_SELECTOR,
    "div[class*='Modal_modal__container'] button[class*='Modal_modal__close']"
)

BUNS_TAB = (By.XPATH, '//h2[normalize-space() = "Булки"]')
SAUCES_TAB = (By.XPATH, '//h2[normalize-space() = "Соусы"]')
FILLINGS_TAB = (By.XPATH, '//h2[normalize-space() = "Начинки"]')

INGREDIENT_MODAL_TITLE = (By.XPATH, '//h2[normalize-space() = "Детали ингредиента"]')

INGREDIENT_BUNS = (By.CSS_SELECTOR, "a[href^='/ingredient/']:first-of-type")
INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='counter_counter__num']")
BASKET_SLOT = (
    By.CSS_SELECTOR,
    "li[class*='BurgerConstructor_basket__listItem']"
)

ORDER_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Оформить заказ' or .//span[normalize-space()='Оформить заказ']]"
)

ORDER_STATUS = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")

ORDER_NUMBER_IN_MODAL = (
    By.CSS_SELECTOR,
    "div[class*='Modal_modal__container'] h2[class*='Modal_modal__title']"
)
