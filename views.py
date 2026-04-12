from app import app
from flask import render_template

# routes


# home
@app.route("/")
def home():
    return render_template("index.html")


# contacts
@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


# users
@app.route("/users/<user>")
def homepage(user):
    return render_template("users.html", user = user)
