from flask import Flask
from scrapeutil import get_db

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def get_hello_world():
    return "Hello World"