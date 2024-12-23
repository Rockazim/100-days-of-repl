"""It's time for more bingo! You can reuse your code from day 43, but this time add the following features:

Repeatedly ask the user what number comes up next.
Check the bingo card to see if the number picked matches one on the card.
If the bingo card is all 'X's, then the user has won."""

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
    


while True:
    counter = 0
    question = int(input("What did you get? "))
    for i in range(len(bingo_card)):
        for col in range(len(bingo_card)):
            if question == bingo_card[i][col]:
                bingo_card[i][col] = "X"
    
    for x in bingo_card:
        for y in x:
            if y == "X":
                counter += 1                        
            

    print(f"{bingo_card[0][0]:<5}|{bingo_card[0][1]:^5}|{bingo_card[0][2]:>5}")
    print("--------------------")
    print(f"{bingo_card[1][0]:<5}|{bingo_card[1][1]:^5}|{bingo_card[1][2]:>5}")
    print("--------------------")
    print(f"{bingo_card[2][0]:<5}|{bingo_card[2][1]:^5}|{bingo_card[2][2]:>5}") 

    if counter == 8:
        print("You have won")