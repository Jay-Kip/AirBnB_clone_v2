#!/usr/bin/python3
'''
Flask app
'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    '''
    home route
    '''
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
    c route
    '''
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    '''
    python route
    '''
    return f"Python {text.repace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    '''
    number route
    '''
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    Number template
    '''
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_even(n):
    '''
    Even or odd route
    '''
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, is_even=True)
    else:
        return render_template('6-number_odd_or_even.html', n=n, is_even=False)


if __name__ == "__main__":
    strict_hashes = False
    app.run(host='0.0.0.0', port=5000)
