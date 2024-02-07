import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def instAddFunc(username, password, account_name):
    options = Options()
    options.add_argument("--headless")  # Running in headless mode
    driver = webdriver.Firefox(options=options)

    try:
        logging.debug("Opening Instagram")
        driver.get("https://www.instagram.com")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        logging.debug("Logging in")
        username_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Close Friends']")))
        
        logging.debug("Navigating to close friends list")
        driver.get("https://www.instagram.com/accounts/close_friends/")

        logging.debug(f"Adding {account_name} to close friends")
        account_to_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//span[text()='{account_name}']/ancestor::div[@role='button']"))
         )
        account_to_click.click()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()
        logging.debug("Driver quit")

# Remember to replace 'your_username', 'your_password', and 'account_name' with actual values when calling the function.
# instAddFunc('your_username', 'your_password', 'account_name')

