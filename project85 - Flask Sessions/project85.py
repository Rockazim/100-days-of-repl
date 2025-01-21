from flask import Flask, request, url_for, session
from flask.helpers import redirect
from replit import db
import os

app = Flask(__name__)
app.secret_key = os.environ['sessionKey']



@app.route('/')
def main():
    if session.get("myName"):
        return redirect('loggedin')
    f = open("html/mainpage.html", "r")
    page = f.read()
    f.close()

    return page

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if session.get("myName"):
        return redirect('loggedin')
        
    if request.method == "POST" and request.form["username"] not in db.keys():
        db[request.form["username"]] = {"password": request.form["password"], "name" : request.form["name"]}
        return redirect('/login')
    elif request.method == "POST" and request.form["username"] in db.keys():
        return "Username already taken"

    a = open("html/signup.html")
    page = a.read()
    a.close()
    return page

@app.route('/login', methods =  ["GET", "POST"])
def login():
    if session.get("myName"):
        return redirect('/loggedin')

    elif request.method == "POST" and request.form["username"] in db.keys() and db[request.form["username"]]["password"] == request.form["password"]:
        session["myName"] = request.form["username"]
        return redirect('/loggedin')

    a = open("html/login.html")
    page = a.read()
    a.close()
    return page

@app.route('/loggedin')
def loggedin():
    if session.get("myName"):
        pass
    else:
        return redirect('/login')

    a = open("html/loggedin.html")
    page = a.read()
    a.close()
    page = page.replace("{name}", session.get("myName"))
    return page

@app.route('/logout')
def logout():
    if session.get("myName"):
        session.clear()

    return redirect('/')


app.run(host='0.0.0.0', port=81)