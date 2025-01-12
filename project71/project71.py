"""Today's challenge is to build a simple login system.

Your program should:

Display a menu with the ability to add a user or login.
'Add' user should:
Ask for a username and password.
Create a new password and a randomly generated 4 digit salt.
Append the salt to the password and hash it.
Store the hash and the salt in a repl db with the username as the key.
'Login' should:
Get username and password input.
Display a success message if details are correct.
This system should work with multiple users."""
#hashing function no longer works as python uses different hashes upon startup meaning this program will not work as intended
from replit import db
import random

def add():
    userName = input("Username: ").lower()
    password = input("Password: ")
    salt = random.randint(1000, 9999)
    newPassword = f"{password}{salt}"
    newPassword = hash(newPassword)
    db[userName] = {"password": newPassword, "salt": salt}

def login():
    userName = input("Username: ").lower()
    password = input("Password: ")
    salt = db[userName]["salt"]
    newPassword = f"{password}{salt}"
    newPassword = hash(newPassword)

    if newPassword == db[userName]["password"]:
        print("Logged in")
    else:
        print("Does not exist!")


while True:
    print("🌟Login System🌟\n")
    try:
        choice = int(input("1: New User\n2: Login\n> "))
    except:
        print("Please use a number!")

    if choice == 1:
        add()
    elif choice == 2:
        login()
    else:
        continue
