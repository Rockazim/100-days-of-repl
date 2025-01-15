"""html + css -> day number + title
link to code
soem text with reflections

then add the changing number factor 
which is assumed fromt emplate

hint: use a 2d dict {"74 : {code : "link", reflect : "asdas"}}"""

from flask import Flask

app = Flask(__name__,static_url_path="/static")

pages = {"76" : {"link": "https://tinyurl.com/436p37vb", "reflection" : "Today's challenge is to create a Flask web server with two website endpoints."}, 
         "77": {"link": "https://tinyurl.com/39s7ffeh", "reflection" : "Today's challenge is to set up a simple template for a blog."}
                }

@app.route('/<pageNumber>')
def index(pageNumber):
    link = ""
    reflection = ""
    link = pages[pageNumber]["link"]
    reflection = pages[pageNumber]["reflection"]
    f = open("template/template.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{number}", pageNumber)
    page = page.replace("{url}", link)
    page = page.replace("{reflection}", reflection)
    return page

app.run(host='0.0.0.0', port=81)