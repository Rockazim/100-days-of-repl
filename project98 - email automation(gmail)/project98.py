import random
import schedule
import time, os, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


password = os.environ['mailPassword']
username = os.environ['mailUsername']

f = open("quotes.txt", "r")
great = f.read()
f.close()
new_andimproved = great.split("', '")

def send_mail():
    random_choice = random.randint(0, len(new_andimproved)-1)
    
    
    email = f"{new_andimproved[random_choice]}"
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port = port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart() # Creates the message
    msg['To'] = "EMAIL" # Sets the receiver's email address
    msg['From'] = username # Sets the sender's email address
    msg['Subject'] = "Quote" # Sets the subject of the message
    msg.attach(MIMEText(email, 'html')) 
    s.send_message(msg) # Sends the message
    del msg



def job():
    print("Sending message")
    send_mail()

schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)