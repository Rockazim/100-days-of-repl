"""Look out, Big Brother! Today is a project day and you are going to build your own private diary to keep your innermost thoughts secret from the world.

Your diary should:

Set an access password.
Prompt the user to type in a password.
If they don't get the password right, exit the program.
If they get it right, they enter the main menu, which gives 'Add' or 'View' diary entries.
Choosing 'add' should:
Prompt the user to type the entry and store it in the database with the timestamp as the key.
Choosing 'view' should:
Show the user the previous (most recent) entry.
They can then choose to see the next previous entry working backwards until they get to the end. Or exit back to the menu."""
from replit import db
import datetime

def add():
    timestamp = datetime.datetime.now()
    diary = input(f"Diary entry for {timestamp}")
    db[timestamp] = 

def main():
    while True:
        try:
            choice = int(input("1: Add\n2:View\n> "))
        except:
            print("Please enter a valid choice!")

        if choice == 1:
            add()
        elif choice == 2:
            view()
        else:
            continue


pw = input("Whats the password > ")
if pw == "123":
    main()
else:
    print("Wrong password! ")
    exit()