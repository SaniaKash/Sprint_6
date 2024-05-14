from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import driver
from url import MAIN_PAGE_URL
from locators.main_page_locator import MainPageLocators


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigation(self):
        return self.driver.get(MainPageLocators.MAIN_PAGE_URL)

    def find_element(self, locator):
        element = self.find_element(locator)
        return element

    def click_element(self, locator):
        element = self.find_element(locator)
        return element.click()

    def execute_script(self, locator):  # Скролл страницы до элемента
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_visible(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        return element.send_keys(text)





