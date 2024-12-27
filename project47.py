
"""Alright Top Trumpers. Your program should work like this.

Pick a category. Something popular. You know like 'most handsome computer science teachers'. 😆
Store the information of two different objects in a 2D dictionary.
The key field should be name.
The data in the sub dictionary should be some stats about the object. For example:
Intelligence
Handsomeness
L33t c0ding skillz
Baldness level
Use an infinite loop to get the user to pick one of the two cards, then pick a stat from that card.
Display the chosen stat for both cards and output which has won.
🥳 Extra points for:

Making the dictionary dynamic so you can add your own cards.
Using a loop to play the game in a 2 player format, keeping track of points scored."""

import random

characters = {"Lamborghini" : {"hp": 700 , "engine": 12, "model":2012}, 
              "Maserati" :{"hp":621 , "engine":6, "model": 2020},
                "Porsche" : {"hp": 500, "engine": 5, "model": 2015}, 
                "Pagani" : {"hp":720, "engine":11, "model":2012}} 



def character_selection():
    
    for i, x in characters.items():
        print(i)

def computer_choice(avoid):
    while True:
        random_choice = random.randint(0,3)
        if random_choice == 0 and avoid != "Lamborghini":
            print("Computer has picked Lamborghini")
            return "Lamborghini"
        elif random_choice == 1 and avoid != "Maserati":
            print("Computer has picked Maserati")
            return "Maserati"
        elif random_choice == 2 and avoid != "Porsche":
            print("Computer has picked Porsche")
            return "Porsche"
        elif random_choice == 3 and avoid != "Pagani":
            print("Computer has picked Pagani")
            return "Pagani"
        else:
            continue
def compare(pick1, pick2, stat):
    print()
    print(f"{pick1} has a {stat} of {characters[pick1][stat]}")
    print(f"{pick2} has a {stat} of {characters[pick2][stat]}\n")
    if characters[pick1][stat] > characters[pick2][stat]:
        print(f"{pick1} wins!")
    elif characters[pick1][stat] < characters[pick2][stat]:
        print(f"{pick2} wins!")
    else:
        print("Error!")

print("Top Trumps")
print("----------\n")
while True:
    print("Characters\n")
    character_selection()
    print("")
    human = input("Pick your character\n>").capitalize()
    print("")
    computer = computer_choice(human)
    stat_choice = input("Choose your stat: HP, Engine, Model\n>").lower()
    compare(human, computer, stat_choice)

    again = input("Again? (y/n) ").lower()
    if again == "y":
        continue
    else:
        break
