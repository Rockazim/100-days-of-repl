"""Your program should:

Ask the user to input their three letter initials and score (out of about 100,000).
Save both those values into a file called 'high.score'.
This should use append mode. If the file doesn't exist, it should be created. If it does, the score should be added to the end.
Each new entry score should go on a new line as initials space score. Then start a new line for the next entry.
Add 2-3 scores for testing in a loop.
The loop should ask the user if they've finished entering data and stop if they have.
🥳 Extra points for getting all the inputs with just one input command and the split function."""

f = open("'high.score.txt", "a")
print("HIGH SCORE TABLE\n")
for i in range(3):
    initial = input("INITIALS >").capitalize()
    score = int(input("SCORE >"))
    print("\nADDED")
    f.write(f"{initial} {score}\n")
f.close()