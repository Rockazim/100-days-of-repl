from flask import Flask, request, redirect, session
from replit import db
import os

app = Flask(__name__)

app.secret_key = os.environ['sessionKey']



@app.route('/', methods = ["GET", "POST"])
def main():
    if session.get("myName"):
        return redirect('/loggedin')
    f = open("html/mainpage.html", "r")
    page = f.read()
    f.close()

    page2= ""
    keys = db.keys()
    for x in keys:
        b = open("html/template.html", "r")
        page2 = b.read()
        b.close()
        page2 = page2.replace("{Title}", x)
        page2 = page2.replace("{Date}", db[x]["Date"])
        page2 = page2.replace("{Body}", db[x]["Text"])
        page = page + page2


    return page

@app.route('/login', methods = ["GET", "POST"])
def login():
    if session.get("myName"):
        return redirect('/loggedin')
    form = request.form
    if request.method == "POST" and form["username"] == "a" and form["password"] == "a":
        session["myName"] = request.form["username"]
        return redirect('/loggedin')
    f = open("html/login.html", "r")
    page = f.read()
    f.close()
    return page

@app.route('/loggedin', methods = ["GET", "POST"])
def loggedin():
    if session.get("myName"):
        pass
    else:
        return redirect('/')
    page2 = ""
    if request.method == "POST":
        form = request.form
        db[form["title"]] = {"Date" : form["date"], "Text" : form["bodyoftext"]}

    f = open("html/loggedin.html", "r")
    page = f.read()
    f.close()

    keys = db.keys()
    for x in keys:
        b = open("html/template.html", "r")
        page2 = b.read()
        b.close()
        page2 = page2.replace("{Title}", x)
        page2 = page2.replace("{Date}", db[x]["Date"])
        page2 = page2.replace("{Body}", db[x]["Text"])
        page = page + page2

    return page

@app.route('/logout')
def logout():
    if session.get("myName"):
        session.clear()
    return redirect('/')


app.run(host='0.0.0.0', port=81)
