from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome_init():
    return 'welcome'

@app.route("/welcome/<page>")
def welcome(page):
    return f"welcome {page}"