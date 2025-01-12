"""Now that we know about secure passwords, we can really protect our diary program.

Go back 10 days and grab your diary code from Day 62.

When you have it, add the following features:

The first time the diary is run, the user must create a username and password.
Salt & hash the password and store it in the database with the username as the key.
Then proceed to the diary.
The next time that program is run, it should prompt for the username and password, and only allow access if they are correct.
The username, password, and salt should be excluded from diary entry outputs, for obvious reasons."""
from replit import db
import hashlib
import datetime
import random
import os
import time

def hash_password(password, salt):
    """Hashes the password with the salt using SHA-512."""
    combined = f"{password}{salt}".encode('utf-8')
    return hashlib.sha512(combined).hexdigest()

def create_user():
    """Creates a new user with a hashed password."""
    user_name = input("Set Username: ").lower()
    password = input("Set Password: ")
    salt = random.randint(1000, 9999)
    hashed_password = hash_password(password, salt)
    db[f"user_{user_name}"] = {"password": hashed_password, "salt": salt}
    print("Account created successfully!")
    time.sleep(2)
    os.system("clear")

def login():
    userName = input("Username: ").lower()
    password = input("Password: ")
    user_key = f"user_{userName}" 
    salt = db[user_key]["salt"]
    newPassword = hash_password(password, salt)

    if newPassword == db[user_key]["password"]:
        print("Login Successful!")
        time.sleep(1)
        os.system("clear")
        return True
    else:
        print("Login Failed!")
        time.sleep(1)
        os.system("clear")
        return False

def add():
    timestamp = str(datetime.datetime.now())
    diary = input(f"Diary entry for {timestamp}\n")
    timestamp = f" {timestamp}"
    db[timestamp] = diary


def view():
    entries = db.prefix(" ")
    entries = entries[::-1]
    try:
        selection = int(input("1: Most recent?\n2: View exact diary?\n>"))
    except:
        print("Please use a valid response!")
        view()

    if selection == 1:
        for i in entries:
            print(f"{i}\n {db[i]}\n", sep="")
            if input("Next or exit? > ").lower() == "next":
                continue
            else:
                break
    elif selection == 2:
        year = int(input("Input the year> "))
        month = int(input("Input the month> "))
        day = int(input("Input the day> "))

        user_date = str(datetime.date(year, month, day))
        for i in entries:
            if i[1:11] == user_date:
                print(f"{i}\n {db[i]}\n", sep="")
            else:
                continue

    else:
        view()


def main():
    while True:
        try:
            choice = int(input("1: Add\n2: View\n> "))
        except:
            print("Please enter a valid choice!")

        if choice == 1:
            add()
        elif choice == 2:
            view()
        else:
            continue


def check_user():
    for x in db.keys():
        if x[0:4] == "user":
            return True
        
    return False

if check_user() == True:
    if login() == True:
        main()
    else:
        print("Doesn't exist!")
        exit()
elif check_user() == False:
    print("Need to create an account!")
    time.sleep(1)
    os.system("clear")
    create_user()
    if login() == True:
        main()
    else:
        exit()
