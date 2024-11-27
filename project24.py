"""Create subroutines that will roll a dice with any number of
 sides (essentially as big of a number as you like). Write one 
 subroutine with one parameter that allows us to call a function (such as rollDice).
"""

import random

def randomroll(sides):
    while True:
        roll = random.randint(1, sides)
        print("You rolled", roll)

        again = input("Roll again? ")
        if again == "Yes":
            continue
        else:
            exit()

    
print("Infinity Dice!")
sides = int(input("How many sides?: "))
randomroll(sides)
    
