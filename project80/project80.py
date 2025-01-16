from flask import Flask, request

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    page = ""
    form = request.form
    if form["Username"] == "Azim" and form["password"] == "1":
        page += "You are logged in."
    elif form["Username"] == "Tyrone" and form["password"] == "2":
        page += "You are logged in."
    elif form["Username"] == "Yung" and form["password"] == "3":
        page += "You are logged in."
    else:
        page += "Username or password incorrect!"
    return page

@app.route('/')
def index():
    f = open("template/project79.html", "r")
    page = f.read()
    f.close()
    return page



app.run(host='0.0.0.0', port=81)