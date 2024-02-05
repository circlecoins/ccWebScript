from flask import Flask, request
import threading
import json

app = Flask(__name__)


@app.route('/run_script')
def run_script():
    return {"status": "Script is running"}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
