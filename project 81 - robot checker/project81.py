from flask import Flask, request

app = Flask(__name__)


@app.route("/process", methods = ["POST"])
def process():
    form = request.form
    if form["answer"] == "No" and form["emotions"] == "Yea sometimes" and form["infinity"].lower() == "infinity":
        return "Hi there fellow human"
    else:
        return "You're a bot begone!"

@app.route('/')
def index():
    f = open("template/project81.html", "r")
    page = f.read()
    f.close()
    return page

app.run(host='0.0.0.0', port=81)