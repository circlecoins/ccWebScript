from flask import Flask, request
import threading

from main import open_instagram_and_click_account

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
    app.run(debug=True, host='0.0.0.0', port=5000)
