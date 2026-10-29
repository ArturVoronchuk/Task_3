from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, timeout=None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout)

    def js_click(self, locator, timeout=10):
        element = self._wait(timeout).until(
            ec.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)
        return self

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_overlay_disappears(self, overlay_locator, timeout=15):
        if overlay_locator is None:
            return self
        self._wait(timeout).until(
            ec.invisibility_of_element_located(overlay_locator)
        )
        return self

    def find_visible_element(self, locator):
        return self._wait().until(ec.visibility_of_element_located(locator))

    def click_to_element(self, locator, overlay_locator=None):
        if overlay_locator:
            self.wait_overlay_disappears(overlay_locator)
        element = self._wait().until(ec.element_to_be_clickable(locator))
        element.click()
        return self

    def send_keys(self, locator, text, overlay_locator=None):
        if overlay_locator:
            self.wait_overlay_disappears(overlay_locator)
        element = self._wait().until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return self

    def is_element_present(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_until_invisible(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout, poll_frequency=0.5)
        try:
            wait.until(ec.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        return self

    def drag_and_drop_js(self, source_locator, target_locator):
        source = self._wait(10).until(ec.presence_of_element_located(source_locator))
        target = self._wait(10).until(ec.presence_of_element_located(target_locator))

        js_script = """
        const src = arguments[0], dst = arguments[1];
        const dt = new DataTransfer();

        const fire = (el, type) => el.dispatchEvent(
            new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: dt})
        );

        fire(src, 'dragstart');
        fire(dst, 'dragenter');
        fire(dst, 'dragover');
        fire(dst, 'drop');
        fire(src, 'dragend');
        """
        self.driver.execute_script(js_script, source, target)
        return self

    def get_text(self, locator, timeout=None):
        element = self._wait(timeout).until(
            ec.visibility_of_element_located(locator)
        )
        return element.text.strip()

    def get_text_when(self, locator, condition, timeout=10):
        self._wait(timeout).until(
            lambda d: condition(self.get_text(locator))
        )
        return self.get_text(locator)