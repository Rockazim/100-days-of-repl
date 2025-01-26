import requests,json
import time
from replit import db
import os

while True:
    result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
    joke = result.json()
    print(joke["joke"])
    time.sleep(1)
    question = input("\n(s)ave joke, (l)oad joke, (n)ew joke\n>").lower()
    if question[0] == "s":
        print("Saved")
        db[joke["id"]] = {"joke" : joke["joke"]}
        time.sleep(1)
        os.system("clear")
    elif question[0] == "l":
        for x in db.keys():
            print(f"{db[x]['joke']}", "\n")
        print()
        time.sleep(3)
        os.system("clear")
    elif question[0] == "n":
        continue
    else:
        print("Try again!")
        continue
