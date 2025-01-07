"""Someone is wrong on the Internet!
Today, we're going to fix the major malfunction with social media - other people and their stupid opinions- and create a Twitter for one!

I know you like to hear the sound of your own voice!

Your program should.

Display a menu - Add or View tweets.

'Add' should:

Get the tweet input.
Store it to the database with the current timestamp as the key value.
'View' should:

Show the tweets in reverse chronological order.
Show 10 tweets at a time.
Prompt the user to show another 10 tweets (yes or no).
A 'no' choice goes back to the menu."""


from replit import db
import datetime

messages = []

def add():
    message = input("What do you want to say?\n>")
    timestamp = str(datetime.datetime.now())
    db[timestamp] = message


def view():
    keys = db.keys()
    for key in keys:
      messages.append(key)
    
    count = 1

    for i in messages[::-1]:
        print(db[i])
        count += 1
      
        if count == 10:
          answer = input("See next 10? (y/n) >").capitalize()
          if answer == "Y":
            count = 1
            continue
          else:
            break



while True:
    print("Tweeter")
    try:
        choice = int(input("1: Add Tweet\n2: View Tweets\n>"))
    except:
        print("Please use an integer!")

    if choice == 1:
        add()
    elif choice == 2:
        view()
    else:
        continue
