from flask import Flask, request
from main import open_instagram_and_click_account
import threading
app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_script():
    # Получаем данные из тела запроса в формате JSON
    data = request.json
    username = data['username']
    password = data['password']
    account_name = data['account_name']

    # Запускаем скрипт Selenium в отдельном потоке
    threading.Thread(target=open_instagram_and_click_account, args=(username, password, account_name)).start()

    # Отправляем ответ, что скрипт запущен
    return {"status": "Script is running"}
