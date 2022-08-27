"""Capstone Project 1 for web development"""

from flask import Flask

app = Flask(__name__)

@app.route('/first-route')   # in terminal flask run, in browser http://127.0.0.1:5000/first-route
def first_route():
    return "First Route for the Capstone Porject"