from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Hello, Flask!</p>"

@app.route('/greet/<name>')
def greet(name):
    return f"<p>Hello, {name}!</p>"

@app.route('/bye')
def bye():
    return "<p>Goodbye!</p>"

@app.route('/<name>/<int:number>')
def repeat_name(name, number):
    return f"<p>Hi I'm {name} I'm {number} years old.</p>"