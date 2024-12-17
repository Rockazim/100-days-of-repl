"""Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.

Example:

30 Days Down
Day 1: 
Amazing
            You thought Day 1 was amazing.
Day 2:
so good that I bought the David plushie
              You thought Day 2 was so good...
"""

print("30 Days Down - What did you think?")
for i in range(1, 31):
    print(f"Day {i}:")
    idea = input("")
    text1 = f"You thought Day {i}"
    text2 = f"was {idea}"
    print(f"{text1: ^35}")
    print(f"{text2: ^35}")
