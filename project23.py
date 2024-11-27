"""Create a subroutine with both a username and password.
Create a loop to prompt the user again and again until they put in the correct login information."""

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    if username == "Zim" and password == "zimothy.com":
      print("Welcome to Replit")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")




print("Replit Login System")
login()