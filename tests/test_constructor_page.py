from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import PageLocators
from data import MAIN_URL


def test_transfer_to_bread_section(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.BREAD_SECTION))
    driver.find_element(*PageLocators.FILLINGS_SECTION).click()
    driver.find_element(*PageLocators.BREAD_SECTION).click()

    assert driver.find_element(*PageLocators.FLUO_BREAD).is_enabled()


def test_transfer_to_sauce_section(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.BREAD_SECTION))
    driver.find_element(*PageLocators.FILLINGS_SECTION).click()
    driver.find_element(*PageLocators.SAUCE_SECTION).click()

    assert driver.find_element(*PageLocators.SPICY_X_SAUCE).is_enabled()


def test_transfer_to_sauce_section(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.BREAD_SECTION))
    driver.find_element(*PageLocators.FILLINGS_SECTION).click()

    assert driver.find_element(*PageLocators.MEAT).is_enabled()