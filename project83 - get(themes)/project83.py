from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")


@app.route('/one', methods=["GET"])
def day1():
    
    title = "Hey guys"
    date = "1/10/2025"
    entry = "Ya boy is grinding these repl's on the Daily!!!"
    page = ""
    
    data = request.args.get("template", "").lower()
    
    if data == "":
        f = open("C:/project83/template/template.html", "r")
    
    elif data == "fancy":
        f = open("C:/project83/template/fancytemplate.html", "r")

    elif data == "chill":
        f = open("C:/project83/template/chilltemplate.html", "r")

    page = f.read()
    f.close()
    page = page.replace("{Title}", title)
    page = page.replace("{Date}", date)
    page = page.replace("{Entry}", entry)
    return page

@app.route('/two', methods=["GET"])
def day2():
    title = "LETS GET IT BOYS"
    date = "1/15/2025"
    entry = "Did ya see the game billy?"
    page = ""

    data = request.args.get("template", "").lower()
    
    if data == "":
        f = open("C:/project83/template/template.html", "r")
    
    elif data == "fancy":
        f = open("C:/project83/template/fancytemplate.html", "r")

    elif data == "chill":
        f = open("C:/project83/template/chilltemplate.html", "r")

    page = f.read()
    f.close()
    page = page.replace("{Title}", title)
    page = page.replace("{Date}", date)
    page = page.replace("{Entry}", entry)
    return page

@app.route('/1')
def dayone():
    return redirect('/one')
    
@app.route('/2')
def daytwo():
    return redirect('/two')

app.run(host='0.0.0.0', port=81)
