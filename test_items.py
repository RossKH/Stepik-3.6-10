from selenium.webdriver.common.by import By
import time
link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_bucket(browser):
    browser.get(link)
    time.sleep(2)
    try:
        button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert button is not None, "Кнопка не найдена на странице"
    except NoSuchElementException:
        assert False, "Кнопка не найдена на странице"