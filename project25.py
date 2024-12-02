"""Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.
(We genuinely see this in video games!)

🥳 Extra points if you ask for the character's name and double extra points if you use different colors!"""


"""⚔️ Character Stats Generator ⚔️

Name your warrior: Agnes
Their health is: 20hp

Name your warrior: Ian
Their health is: 6hp

Name your warrior: Penelope
Their health is: 48hp"""

import random

def randomroll(sides):
    numberOfSides = random.randint(1, sides)
    return numberOfSides

def multiply():
    sixDice = randomroll(6)
    eightDice = randomroll(8)
    result = sixDice * eightDice
    return result


print("⚔️ Character Stats Generator ⚔️")

while True:
    name = input("Name your warrior: ")
    health = multiply()
    print("Their health is", health, "hp")

    again = input("Would you like to go again? (Y/N): ")
    if again == "Y":
        continue
    else:
        print("Bye!")
        break