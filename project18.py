#build a "Guess the Number" guessing game.

variable = 690000

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

