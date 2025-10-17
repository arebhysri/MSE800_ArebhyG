from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "<p>Hello, Flask!</p>"