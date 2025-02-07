from replit import db
import requests
from bs4 import BeautifulSoup
import schedule
import time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

password = os.environ['mailPassword']
username = os.environ['mailUsername']


db["Fujifilm GFX 100S"] = {
  "link" : "https://www.wexphotovideo.com/fujifilm-gfx-100s-ii-with-gf-35-70mm-f4-5-5-6-wr-lens-3204540/", "price" : 5300, "desiredprice" : 4700}


db["DJI Osmo Action"] = {
  "link" : "https://www.wexphotovideo.com/dji-osmo-action-4-adventure-combo-3117766/", "price" : 379.00, "desiredprice" : 350}

def send_mail():
    message = ""
    website_calls()
    if db["Fujifilm GFX 100S"]["price"] < db["Fujifilm GFX 100S"]["desiredprice"]:
        message += f"This item: {db['Fujifilm GFX 100S']['link']} is now {db['Fujifilm GFX 100S']['price']} which is below your purchase level of {db['Fujifilm GFX 100S']['desiredprice']}\n"
    if db["DJI Osmo Action"]["price"] < db["DJI Osmo Action"]["desiredprice"]:
        message += f"This item: {db['DJI Osmo Action']['link']} is now {db['DJI Osmo Action']['price']} which is below your purchase level of {db['DJI Osmo Action']['desiredprice']}\n"
    if message == "":   
        return 0 

    email = f"{message}"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port = port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart() # Creates the message
    msg['To'] = "EMAIL" # Sets the receiver's email address
    msg['From'] = username # Sets the sender's email address
    msg['Subject'] = "Product is cheaper" # Sets the subject of the message
    msg.attach(MIMEText(email, 'html')) 
    s.send_message(msg) # Sends the message
    del msg

def website_calls():
    response = requests.get(db["Fujifilm GFX 100S"]["link"])
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    prices = soup.find("span", class_="price wex-red")
    price = prices.text
    price = price.replace(",", "")
    price = price.replace("£", "")
    price = float(price)
    db["Fujifilm GFX 100S"]["price"] = price

    time.sleep(1)

    response_2 =  requests.get(db["DJI Osmo Action"]["link"])
    html = response_2.text
    soup = BeautifulSoup(html, 'html.parser')
    prices = soup.find("span", class_="price wex-red")
    price = prices.text
    price = price.replace(",", "")
    price = price.replace("£", "")
    price = float(price)
    db["DJI Osmo Action"]["price"] = price

def job():
    print("Sending message")
    send_mail()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)