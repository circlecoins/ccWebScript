from flask import Flask, request, jsonify
from main import open_instagram_and_click_account
import threading
import json

app = Flask(__name__)


@app.route('/run_script', methods=['POST'])
def run_script():
    data = request.json
    username = data['username']
    password = data['password']
    account_name = data['account_name']

    # Запускать скрипт Selenium в отдельном потоке, чтобы не блокировать веб-сервер
    threading.Thread(target=open_instagram_and_click_account, args=(username, password, account_name)).start()

    return {"status": "Script is running"}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
