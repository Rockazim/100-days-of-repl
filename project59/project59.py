"""You're going to write a program that checks a string to see if it is a palindrome.

Yes. We know that Python has the built in function string.reverse() that you could use.

Zero points for that today, we want you to think hard and utilize your skills in:

recursion
string slicing
looping
Your program should:

Prompt the user to input a word.
Analyze the word to see if it is a palindrome.
Output a relevant 'yes/no message."""



"""
#this was my quick solution but I didnt really follow the directions
def is_palidrome(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome. Yay!")
    else:
        print(f"{word} is not a palindrome.")

while True:
    print("🌟Palindrome Checker🌟")
    user_choice = input("Input a word > ")
    is_palidrome(user_choice)

    stop = input("Stop (y/n)").capitalize()
    if stop == "Y":
        break
    else:
        continue
"""

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

while True:
    print("🌟Palindrome Checker🌟")
    user_choice = input("Input a word > ")
    decision = is_palindrome(user_choice)

    if decision == True:
        print(f"{user_choice} is a palindrome. Yay!")
    else:
        print(f"{user_choice} is not a palindrome.")

    stop = input("Stop (y/n)" ).capitalize()
    if stop == "Y":
        break
    else:
        continue