"""an automated game battle system!"""


import random
import os
import time

def charactercreation():
    name = input("Name your legend:\n")
    type = input("Character Type (Human, Elf, Wiard, Orc):\n")
    return name

def healthstats():
    health = (random.randint(1,6) * random.randint(1,12))/2 + 10
    return health

def strengthstats():
    strength = (random.randint(1,6) * random.randint(1,12))/2 + 10
    return strength


print("⚔️ BATTLE TIME ⚔️\n")
time.sleep(1)
player1 = charactercreation()
print()
print(player1)
time.sleep(1)

player1Health = healthstats()
player1Strength = strengthstats()
print("HEALTH:", player1Health)
print("STRENGTH:", player1Strength)

time.sleep(1)
print("\nWho are they battling?\n")
player2 = charactercreation()
print()
print(player2)
time.sleep(1)

player2Health = healthstats()
player2Strength = strengthstats()
print("HEALTH:", player2Health)
print("STRENGTH:", player2Strength)

time.sleep(1)
os.system("clear")

rounds = 1
while True:
    print("⚔️ BATTLE TIME ⚔️\n")

    if rounds == 1:
        print("The battle begins!")
    else:
        print("The battle continues!")
        
    time.sleep(1)
    player1Roll = random.randint(1,6)
    player2Roll = random.randint(1,6)
    attack = abs(player1Strength - player2Strength) + 1

    if player1Roll > player2Roll:
        if rounds == 1:
            print(player1, "wins the first blow")
            print(player2, "takes a hit, with",attack,"damage")
            player2Health = player2Health - attack
        else:
            print(player1, "wins round", rounds)
            print(player2, "takes a hit, with",attack,"damage")
            player2Health = player2Health - attack
    elif player1Roll < player2Roll:
        if rounds == 1:
            print(player2, "wins the first blow")
            print(player1, "takes a hit, with",attack,"damage")
            player1Health = player1Health - attack
        else:
            print(player2, "wins round", rounds)
            print(player1, "takes a hit, with",attack,"damage")
            player1Health = player1Health - attack
    else:
        print("Draw! Neither", player1, "or", player2, "are damaged!")
    time.sleep(1)

    print(player1)
    print(player1Health,"\n")
    print(player2)
    print(player2Health,"\n")
    time.sleep(1)
    
    if player1Health > 0 and player2Health > 0:
        print("And they're both standing for the next round!")
        rounds += 1
        time.sleep(1)
        os.system("clear")
        continue
    elif player1Health < 0:
        print("Oh no", player1, "has died!")
        print()
        print(player2, "destroyed", player1, "in", rounds, "rounds!")
        exit()
    elif player2Health < 0:
        print("Oh no", player2, "has died!")
        print()
        print(player1, "destroyed", player2, "in", rounds, "rounds!")
        exit()
    
    