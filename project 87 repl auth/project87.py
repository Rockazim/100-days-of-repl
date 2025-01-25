from flask import Flask, request, redirect
from replit import db
import os

app = Flask(__name__)


@app.route('/')
def main():
    user_id = request.headers['X-Replit-User-Name']
    if user_id == "aqudrat9778":
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

@app.route('/loggedin', methods = ["GET", "POST"])
def loggedin():
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




app.run(host='0.0.0.0', port=81)