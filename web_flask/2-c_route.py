#!/usr/bin/python3
'''
display “C ” followed by the value of the text variable
'''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    '''
    Route to home page
    '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hnbn():
    '''
    Route to hbnb page
    '''
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    ''''
    Route to c page
    '''
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
