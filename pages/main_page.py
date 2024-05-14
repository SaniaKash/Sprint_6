from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators
from conftest import driver
from selenium.webdriver.chrome.webdriver import WebDriver


class MainPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    # def scooter_main_page(self):
    #    return driver.current_url

    def open_main_page(self):
        self.navigation()

    def click_header_order_but(self):
        self.click_element(*MainPageLocators.ORDER_BUT_HEADER)

    def scroll_to_question(self, locator_question):
        self.execute_script(locator_question)

    def click_question(self, locator_question):
        self.click_element(locator_question)

    def check_open_right_response(self, locator_response):
        response = self.find_element(locator_response).text
        assert response

    def click_scooter_logo(self):
        element = self.find_element(*MainPageLocators.SCOOTER_LOGO)
        return element.click()


