"""In yesterday's challenge, you created a file called high.score and stored some high scores in it.

We've added a version of that file to this repl.

Your program should:

Read in the data from the high.score file.
Identify which of those users had the highest score. Automatically! (Not you doing it!)
Output the name and score of the winner."""

f = open("'high.score.txt", "r")
highest_score = f.read().split()
best = int(highest_score[1])
name = (highest_score[0])
i = 1

while True:
    if best <  int(highest_score[i]):
        best = int(highest_score[i])
        name = (highest_score[i-1])
    i+= 2
    if i > len(highest_score):
        break

print("🌟Current Leader🌟")
print("\nAnalyzing high scores......")
print(f"\nCurrent leader is {name} {best}")
f.close()