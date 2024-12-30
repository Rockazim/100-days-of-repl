"""Day 50! Boy, you are smashing this 100 days! 🎊 To celebrate, here's a project for you.

Your idea storage system should:

Prompt the user to add an idea, or load a random one.
Choosing 'Add an idea' results in:
A prompt for the user to input their idea.
Add the idea to a text file called 'my.ideas'.
Add the idea in append mode, with every new idea on a brand new line.
Choosing 'Load random' results in:
Load the list of ideas.
Choose one at random.
Display it on screen for a few seconds.
Return to the menu."""
import random
import time, os
def random_choice():
    page = open("my.ideas", "r")
    values = page.read().split()
    lines = len(values)
    line_choice = random.randint(0,lines-1)
    print(f"{values[line_choice]}\n")
    time.sleep(2)
    page.close

def add(idea):
    f = open("my.ideas", "a")
    f.write(f"{idea}\n")
    f.close


while True:
    print("IDEAS")
    choice = int(input("\n1: Add an idea\n2: Load up a random idea\n3: Exit\n> "))
    if choice == 1:
        new_idea = input("\nIdea > ")
        add(new_idea)
    elif choice == 2:
        random_choice()
        os.system("clear")
    elif choice ==3:
        break
    else:
        print("Try again!")
        continue

