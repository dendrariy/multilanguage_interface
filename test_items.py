from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMultiLang():
    def test_contains_bucket_button(self, browser):
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button, "Button is not contains on the page"