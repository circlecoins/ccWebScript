from flask import Flask, request
from main import instAddFunc
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
    threading.Thread(target=instAddFunc, args=(username, password, account_name)).start()

    # Отправляем ответ, что скрипт запущен
    return {"status": "Script is running"}
