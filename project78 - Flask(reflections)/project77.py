from flask import Flask, redirect

app = Flask(__name__, static_url_path="/static")


@app.route('/one')
def day1():
    title = "Hey guys"
    date = "1/10/2025"
    entry = "Ya boy is grinding these repl's on the Daily!!!"
    page = ""
    f = open("template/template.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{Title}", title)
    page = page.replace("{Date}", date)
    page = page.replace("{Entry}", entry)
    return page


@app.route('/two')
def day2():
    title = "LETS GET IT BOYS"
    date = "1/15/2025"
    entry = "Did ya see the game billy?"
    page = ""
    f = open("template/template.html", "r")
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