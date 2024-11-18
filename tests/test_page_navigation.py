from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import PageLocators
from data import MAIN_URL


def test_transfer_to_account(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()

    assert driver.find_element(*PageLocators.REG_BUTTON).is_enabled()


def test_transfer_account_to_constructor(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click()

    assert driver.find_element(*PageLocators.COLLECT_BURGER).is_enabled()


def test_transfer_account_to_logo(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*PageLocators.LOGO).click()

    assert driver.find_element(*PageLocators.COLLECT_BURGER).is_enabled()