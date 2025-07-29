from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xpaths import authentication
from time import sleep


def login(driver):
    driver.find_element(By.XPATH, authentication["button_login"]).click()
    driver.find_element(By.XPATH, authentication["fla_id"]).click()

    # Espera pelo campo de usuário
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, authentication["username_path"]))
    )

    driver.find_element(By.XPATH, authentication["username_path"]).send_keys("abcde@gmail.com")
    driver.find_element(By.XPATH, authentication["password_path"]).send_keys("*******")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, authentication["login_button_path"]))
    ).click()

    sleep(3)
