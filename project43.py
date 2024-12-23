"""Randomly generate a series of number between 0 and 90.
Allocate each number to a place in a 2D list.
The numbers should be in numerical order, left to right.
Numbers should not be repeated.
The center square should not contain a number. It should contain the word 'BINGO!'.
When the program is run, the bingo card should be displayed on screen."""


import random 
bingo_card = [["","",""],["","",""],["","",""]]
picked_numbers = []

def randomly_generate():
    while True:
        number = random.randint(1,90)
        if number in bingo_card:
            continue
        else:
            picked_numbers.append(number)
        if len(picked_numbers) == 9:
            picked_numbers.sort()
            break

randomly_generate()

bingo_card[0][0] = picked_numbers[0]
bingo_card[0][1] = picked_numbers[1]
bingo_card[0][2] = picked_numbers[2]
bingo_card[1][0] = picked_numbers[3]
bingo_card[1][1] = "BINGO"
bingo_card[1][2] = picked_numbers[5]
bingo_card[2][0] = picked_numbers[6]
bingo_card[2][1] = picked_numbers[7]
bingo_card[2][2] = picked_numbers[8]

print(f"{bingo_card[0][0]:<5}|{bingo_card[0][1]:^5}|{bingo_card[0][2]:>5}")
print("--------------------")
print(f"{bingo_card[1][0]:<5}|{bingo_card[1][1]:^5}|{bingo_card[1][2]:>5}")
print("--------------------")
print(f"{bingo_card[2][0]:<5}|{bingo_card[2][1]:^5}|{bingo_card[2][2]:>5}")