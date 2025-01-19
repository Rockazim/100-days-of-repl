from flask import Flask, request, url_for
from flask.helpers import redirect
from replit import db

app = Flask(__name__)

@app.route('/')
def main():
    f = open("html/mainpage.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{signup_link}", url_for('signup') )
    page = page.replace("{login_link}", url_for('login'))
    return page

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST" and request.form["username"] not in db.keys():
        db[request.form["username"]] = {"password": request.form["password"], "name" : request.form["name"]}
        return redirect('/login')
    elif request.method == "POST" and request.form["username"] in db.keys():
        return "Username already taken"

    a = open("html/signup.html")
    page = a.read()
    a.close()
    return page

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] in db.keys() and db[request.form["username"]]["password"] == request.form["password"]:
            return f"Hello {db[request.form['username']]['name']}"
        else:
            return "Incorrect username or password"
    a = open("html/login.html")
    page = a.read()
    a.close()
    return page

app.run(host='0.0.0.0', port=81)

