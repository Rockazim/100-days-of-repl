"""Once the word has been picked, the following things need to happen:

Prompt the user to type in a letter.
Check if the letter is in the word.
If it does, output the word with all blanks apart from the letter(s) they've already guessed.
Keep a running list of the letters they've used.
Count how many times they've picked a letter that isn't in the word - more than 6 and they lose.
Output a 'win' message if they reveal all the letters.
🥳 Extra points for using ASCII art to draw the hangman as the player makes incorrect guesses."""

import random
selection = [ "Zesty", "Quagmire", "Nebula", "Rendezvous", "Cerebral", "Mosaic", "Whimsical",  "Arcane", "Fennel", "Cacophony"]
wordChosen = random.choice(selection).lower()
choices = []
stripped_word = []
lives = 6


#create the mask
for a in range(len(wordChosen)):
    choices.append("_")
    stripped_word.append(wordChosen[a])


print(wordChosen)


print("🌟Hangman🌟\n")
while True:
    guess = input("Choose a letter\n").lower().strip()
    if guess in choices:
        print("Duplicate Try again!")
        continue
    elif guess in wordChosen and guess != "":
        print("Correct")
        for i in range(len(wordChosen)):
            if wordChosen[i] == guess:
                choices[i] = guess
        print(choices, "\n")
    else:
        print("Nope, not in there. ")
        lives -= 1
        print(f"{lives} left.")


    if lives == 6:
        print("""
              +---+
              |   |
              |   
              |
              |
              |
              =========""")



    if lives == 5:
        print("""
              +---+
              |   |
              |   O
              |
              |
              |
              =========""")
    elif lives == 4:
        print("""
              +---+
              |   |
              |   O
              |   |
              |
              |
              =========""")

    elif lives == 3:
        print("""
              +---+
              |   |
              |   O
              |  /| 
              |
              |
              =========""")

    elif lives == 2:
        print("""
              +---+
              |   |
              |   O
              |  /|\\
              |
              |
              =========""")

    elif lives == 1:
        print("""
              +---+
              |   |
              |   O
              |  /|\\
              |  / 
              |
              =========""")

    elif lives == 0:   
        print("""
              +---+
              |   |
              |   O
              |  /|\\
              |  / \\
              |
              =========""")

    if lives < 1:
        print("You lost!")
        break
    elif choices == stripped_word:
        print(f"You won with! {lives} lives left.")
        break
