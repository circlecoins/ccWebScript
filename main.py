from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def instAddFunc(username, password, account_name):
    options = Options()
    options.add_argument("--headless")  # Запуск в headless режиме
    driver = webdriver.Firefox(options=options)

    try:
        driver.get("https://www.instagram.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Close Friends']")))
        driver.get("https://www.instagram.com/accounts/close_friends/")

        account_to_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{account_name}']/ancestor::div[@role='button']"))
         )
        account_to_click.click()

    finally:
        driver.quit()
