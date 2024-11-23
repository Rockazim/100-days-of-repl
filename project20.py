"""Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the input command.)
"""

print("List Generator")
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))

for i in range(start, end, increment):
  print(i)