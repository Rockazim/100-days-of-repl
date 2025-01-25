from flask import Flask, request
from replit import db
import datetime

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def main():
    user_id = request.headers['X-Replit-User-Name']
    if request.method == "POST":
        form = request.form
        if form["message"]:
            timestamp = datetime.datetime.now()
            db[timestamp] = {"message" : form["message"], "user" : user_id}
        else:
            for x in range(5):
                if str(x) in form.keys():
                    get_rid(int(x))
                    
    f = open("html/chat.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{username}", user_id)
    page = page.replace("{content}", userchats())

    return page

def userchats():
    user_id = request.headers['X-Replit-User-Name']

    if user_id == "aqudrat9778":
        f = open("html/adminchat.html", "r")
        page = f.read()
        f.close()
    else:
        f = open("html/userchats.html", "r")
        page = f.read()
        f.close()

    content = ""
    key = db.keys()
    key = list(key)
    counter = 0
    for x in reversed(key):
        temp = page
        user = db[x]["user"]
        message = db[x]["message"]

        temp = temp.replace("{User}", user)
        temp = temp.replace("{Message}", message)
        temp = temp.replace("{timestamp}", x)
        if user_id == "aqudrat9778":
            temp = temp.replace("{button_timestamp}", f"{counter}")

        content = content + temp
        counter += 1
        if counter == 5:
            break
    return content

def get_rid(x):
    count = 0
    for y in reversed(list(db.keys())):
        if x == count:
            del db[y]
        count += 1
        if count==5:
            break
    
app.run(host='0.0.0.0', port=81)