import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Wlcome1"

app.route('/how are you')
def hello():
    return 'I am good'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8084)