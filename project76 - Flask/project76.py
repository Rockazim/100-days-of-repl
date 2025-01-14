from flask import Flask # Imports the flask library

app = Flask(__name__, static_url_path="/static") # Starts the Flask application. The 'app' variable is very important. We'll be using that later.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    page = f"""<html><body>
    <p><a href = "/portfolio">Go to my portfolio</a></p>
    <p><a href = "/linktree">Go to my linktree</a></p>
    </body>
    </html>"""
  
    return page

@app.route('/portfolio')
def portfolio():
    page = """<html>
<head>
  <title>My portfolio</title>
  <link href="static/css/style1.css" rel="stylesheet" type="text/css">
</head>
<body>
  <h1 class="title">Azim's Portfolio</h1>
  <h2>Project 56</h2>
  <a href="https://github.com/AzimQudrat/100-days-of-repl/tree/main/project56">
    <img src="static/images/project56.JPG" width=30%>
  </a>
  <p>For day 56, we organized a dataset of the most streamed songs by creating folders for each artist and
    generating text files for their songs. This project efficiently transformed raw data into a structured format.
  </p>
  <h2>Project 61</h2>
  <a href="https://github.com/AzimQudrat/100-days-of-repl/tree/main/project61">
    <img src="static/images/project61.JPG" width=30%>
  </a>
  <p>For day 61, we created a simple "Twitter for one" program that lets users add and view their own tweets.
    Tweets are stored with timestamps, displayed in reverse chronological order, and shown 10 at a time, making
    it an efficient way to organize personal thoughts.
  </p>
  <h2>Project 53</h2>
  <a href="https://github.com/AzimQudrat/100-days-of-repl/blob/main/project53.py6">
    <img src="static/images/project53.JPG" width=30%>
  </a>
  <p>For day 53, we built a video game inventory system that allows users to add, view, and remove items.
    Items are stored in a file with auto-save and auto-load functionality. The program displays item counts,
    handles duplicates, and ensures an organized inventory experience.
  </p>
  <h2>Project 55</h2>

  <a href="https://github.com/AzimQudrat/100-days-of-repl/blob/main/project55.py">
    <img src="static/images/project55.JPG" width=30%>
  </a>
  <p>For day 55, we enhanced a to-do list management system by adding a backup feature. The program
    creates a "Backups" folder, generates random filenames, and saves a copy of the data before the main
    auto-save. This ensures data integrity and provides a reliable way to recover tasks if needed.
  </p>
  <h2>Project 59</h2>
  <a href="https://github.com/AzimQudrat/100-days-of-repl/tree/main/project59">
    <img src="static/images/project59.JPG" width=30%>
  </a>
  <p>For day 59, we created a program to check if a word is a palindrome using recursion, string slicing, and
    looping. Users input a word, and the program determines if it reads the same forward and backward, outputting
    a clear "yes" or "no" message.
  </p>
</body>
</html>"""
    return page

@app.route('/linktree')
def linktree():
    page = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="static/css/style2.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <img src="static/images/headshot.JPG">
    <h1>Azim Qudrat</h1>
    <p>Software dev</p>
    <h2>Socials</h2>
    <p><a href = "https://github.com/AzimQudrat">Github</a></p>
    <p><a href = "https://www.linkedin.com/in/azimqudrat/">LinkedIn</a></p>
    <p><a href ="https://github.com/AzimQudrat/100-days-of-repl/tree/main/project56">Csv Sorter</a></p>
  
</body>

</html>
"""
    return page



app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.