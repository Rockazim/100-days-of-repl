"""Try to use recursion to build a factorial program.

Yep, it's a math challenge. Recursion is often good for this type of problem.

It could be a real head scratcher, so don't be afraid to use 100 Days of Code Community or the Discord channel for help.

A factorial is the product of all the numbers up to a value, starting from 1.

For example, factorial 5 would be 1 * 2 * 3 * 4 * 5 = 120

Write a function that:
Starts at the highest number.
Multiplies that by factorial of itself minus one
Terminates when it reaches 1 and returns 1
Outputs the factorial."""

def factorial(value, target):
    
    if value == 0:
        print(f"The factorial is {target}")
        return 1
    else:  
        target *= value
        factorial(value - 1, target)

target = 1
print("🌟Factorial Finder🌟")
try:
    choice = int(input('\nInput a number > '))
    factorial(choice, target)
except:
    print("Error please use an integer!")
