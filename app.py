"""Capstone Project 1 for web development"""

from flask import Flask, render_template
# flask debug toolbar import
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

#  flask debut toolbar setup
app.config['SECRET_KEY'] = "it-is-so-secret"
debug = DebugToolbarExtension(app)

##############################################################

# For set project setup, remove once everything is setup properly

@app.route('/first-route')   # in terminal flask run, in browser http://127.0.0.1:5000/first-route
def first_route():
    return "First Route for the Capstone Porject"

@app.route('/first-template')
def first_template():
    return render_template('/first.html')


##############################################################