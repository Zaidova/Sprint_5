from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from data import MAIN_URL
from data import RegistrationData


def test_log_out(driver):
    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*PageLocators.INPUT_EMAIL_ENT).send_keys(RegistrationData.EMAIL)
    driver.find_element(*PageLocators.INPUT_PASS).send_keys(RegistrationData.PASSWORD)
    driver.find_element(*PageLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PageLocators.SET_ORDER_BUTTON))
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.EXIT_BUTTON))
    driver.find_element(*PageLocators.EXIT_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(PageLocators.LOGIN_BUTTON))

    assert driver.find_element(*PageLocators.LOGIN_BUTTON).is_enabled()