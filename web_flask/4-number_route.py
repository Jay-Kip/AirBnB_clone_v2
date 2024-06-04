#!/usr/bin/python3
'''
display “n is a number” only if n is an integer
'''

from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''
    hbnb route
    '''
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    '''
    C route
    '''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text', 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    '''
    Python route
    '''
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number_route(n):
    '''
    Number route
    '''
    return f"{n} is a number"


if __name__ == "__main__":
    strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
