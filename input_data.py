from locators.rent_page_locators import RentPageLocators
from locators.order_page_locators import OrderPageLocators


class User1:
    text_name = 'лера'
    text_surname = 'петровна'
    text_address = 'соколиная'
    text_metro = 'Черкизовская'
    text_tel = '111111111111'
    text_date = '01.02.2025'
    locator_rent_date_2_days = RentPageLocators.RENT_TIME_FIELD_2_DAYS
    locator_color_black = RentPageLocators.COLOR_FIELD_BLACK


class User2:
    text_name = 'валера'
    text_surname = 'петров'
    text_address = 'леонова'
    text_metro = 'Сокольники'
    text_tel = '222222222222'
    text_date = '01.02.2026'
    locator_rent_date_3_days = RentPageLocators.RENT_TIME_FIELD_3_DAYS
    locator_color_grey = RentPageLocators.COLOR_FIELD_GREY
