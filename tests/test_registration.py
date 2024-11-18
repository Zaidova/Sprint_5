from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import PageLocators
from data import MAIN_URL
from helpers import GenerationData

def test_registration_success(driver):
    name = GenerationData.generate_name()
    email = GenerationData.generate_email()
    password = GenerationData.generate_password()

    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*PageLocators.REG_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PageLocators.INPUT_NAME))
    driver.find_element(*PageLocators.INPUT_NAME).send_keys(name)
    driver.find_element(*PageLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*PageLocators.INPUT_PASS).send_keys(password)
    driver.find_element(*PageLocators.REG_BUTTON_FORM).click()
    driver.find_element(*PageLocators.INPUT_EMAIL_ENT).send_keys(email)
    driver.find_element(*PageLocators.INPUT_PASS).send_keys(password)
    driver.find_element(*PageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PageLocators.ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PageLocators.ACCOUNT_NAME))
    act_name = driver.find_element(PageLocators.ACCOUNT_NAME).get_attribute('value')

    assert name == act_name

def test_registration_invalid_password(driver):
    name = GenerationData.generate_name()
    email = GenerationData.generate_email()
    password = '1'

    driver.get(MAIN_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PageLocators.LOGIN_ACCOUNT_BUTTON))
    driver.find_element(*PageLocators.LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*PageLocators.REG_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PageLocators.INPUT_NAME))
    driver.find_element(*PageLocators.INPUT_NAME).send_keys(name)
    driver.find_element(*PageLocators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*PageLocators.INPUT_PASS).send_keys(password)
    driver.find_element(*PageLocators.REG_BUTTON_FORM).click()

    assert driver.find_element(*PageLocators.INVALID_PASSWORD_MESSAGE).text == 'Некорректный пароль'
