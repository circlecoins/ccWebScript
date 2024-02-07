from flask import Flask, request
from main import instAddFunc  # Ensure this import is correct based on your project structure
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def run_script():
    logging.debug("Received a POST request")
    # Получаем данные из тела запроса в формате JSON
    try:
        data = request.json
        if not data or 'username' not in data or 'password' not in data or 'account_name' not in data:
            logging.error("Missing required parameters in the request")
            return {"error": "Missing required parameters"}, 400

        username = data['username']
        password = data['password']
        account_name = data['account_name']

        # Запускаем скрипт Selenium в отдельном потоке
        logging.debug(f"Starting Selenium script for user {username} to add {account_name}")
        threading.Thread(target=instAddFunc, args=(username, password, account_name)).start()

        # Отправляем ответ, что скрипт запущен
        logging.debug("Selenium script started successfully")
        return {"status": "Script is running"}

    except Exception as e:
        logging.error(f"An error occurred while processing the request: {e}")
        return {"error": "An error occurred while processing the request"}, 500

if __name__ == '__main__':
    app.run(debug=True)
