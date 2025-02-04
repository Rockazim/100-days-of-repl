import requests
from bs4 import BeautifulSoup
import random
import schedule
import time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = os.environ['mailPassword']
username = os.environ['mailUsername']

used_urls =[]

def send_mail():
    response = requests.get("https://replit.com/community-hub")
    html = response.text

    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    best_links = soup.find_all("a", {"target": "_blank"})
    urls = [link.get("href") for link in best_links if link.get("href")]
    important_urls = []
    for x in urls:
        if "replit" not in x:
            if "Replit" not in x:
                important_urls.append(x)

    notable_links = ""
    for y in important_urls:
        if y in used_urls:
            continue
        else:
            notable_links += f"{y}\n"
            used_urls.append(y)

    email = f"{notable_links}"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port = port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart() # Creates the message
    msg['To'] = "EMAIL" # Sets the receiver's email address
    msg['From'] = username # Sets the sender's email address
    msg['Subject'] = "Interesting Repl's" # Sets the subject of the message
    msg.attach(MIMEText(email, 'html')) 
    s.send_message(msg) # Sends the message
    del msg

def job():
  print("Sending message")
  send_mail()

schedule.every(1).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)