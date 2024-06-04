#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world! This is Jay"

@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    strict_slashes=False
    app.run(host='127.0.0.1', port=4000,debug=True)
