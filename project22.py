"""Copy and paste your code from Day 18.
We are going to make a change to this project:
Make the number generator completely random between 1 and 
1,000,000. Now, the game will always have the user guess a
 random number each time (now the user can't cheat...)"""


import random

variable = random.randint(1,1000000)

counter = 0
while True:
  counter += 1
  guess = int(input("Guess a number between 1 and 1,000,000: "))
  if guess == variable:
    print("Congrats!")
    print(f"It took you {counter} tries to guess the number!")
    break
  
  elif guess < variable and guess > 0:
    print("Too Low! Try again!")
    continue

  elif guess > variable:
    print("Too High! Try again!")
    continue
    
  elif guess < 0:
    print("Don't do that!")
    exit()