"""Welcome to your first video game creation. 
You will create a video game that creates a character's health
 and attack stats...along with an epic name for your character.

Do not delete today's code. You will be building upon it on Day 28.

Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:


Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:


Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
Wrap it in a loop so the user has the option to create another character.
Example:

Character Builder
Name Your Legend:
Sheila the Almighty
Character Type (Human, Elf, Wiard, Orc):
Human
Sheila the Almighty
HEALTH: 40
STRENGTH: 26
May your name go down in Legend..."""

import random
import os
import time

def charactercreation():
    name = input("Name your legend:\n")
    type = input("\nCharacter Type (Human, Elf, Wiard, Orc):\n")
    print()
    print(name)

def healthstats():
    health = (random.randint(1,6) * random.randint(1,12))/2 + 10
    return health

def strengthstats():
    strength = (random.randint(1,6) * random.randint(1,12))/2 + 10
    return strength

while True:

    os.system("clear")
    time.sleep(1)
    print("Character Builder\n")
    time.sleep(1)
    charactercreation()
    time.sleep(1)
    print("HEALTH:", healthstats())
    print("STRENGTH:", strengthstats())
    time.sleep(1)
    print("\nMay your name go down in Legend...")

    time.sleep(1)
    again = input("Go again? (Y/N)")
    if again == "Y":
        continue
    else:
        print("Bye!")
        exit()
