from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMultiLang():
    def test_contains_bucket_button(self, browser):
        browser.get(link)
        try:
            browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        except NoSuchElementException:
            return False
        return True