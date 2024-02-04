from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_instagram_and_click_account(username, password, account_name):
    # Инициализировать драйвер браузера
    driver = webdriver.Chrome()

    # Открыть страницу Instagram
    driver.get("https://www.instagram.com")

    # Пауза для загрузки страницы
    time.sleep(3)

    # Найти поля для ввода логина и пароля
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    # Ввести логин и пароль
    username_input.send_keys({username})
    password_input.send_keys({password})

    # Нажать кнопку входа
    password_input.send_keys(Keys.ENTER)

    # Пауза для завершения авторизации
    time.sleep(5)

    # Переход на страницу близких друзей
    driver.get("https://www.instagram.com/accounts/close_friends/")

    # Пауза для загрузки страницы
    time.sleep(5)

    # Найти и кликнуть по аккаунту с определенным никнеймом
    account_to_click = driver.find_element(By.XPATH, f"//span[text()='{account_name}']/ancestor::div[@role='button']")
    account_to_click.click()

    # Пауза для загрузки профиля
    time.sleep(3)

    # Закрыть браузер после выполнения необходимых действий
    driver.quit()

# Пример вызова функции
# open_instagram_and_click_account("leva.dsgn", "Realartist99", "twitchyxpalm")
