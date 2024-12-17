"""Create a classic user interface using string manipulation.

Create these two user interfaces 
(below) using everything you know about 
extensions to print statements and f-strings.
The second one is a bit more tricky as it involves alignment.

There are no input statements. 
This is all about using print and variables in interesting ways. 
However, you may want to create a subroutine to 
make the color changing easier (like you did on Day 29)."""

red = "\033[0;31m"
white = "\033[1;37m"
blue = "\033[1;34m"
yellow = "\033[1;33m"
green = "\033[0;32m"
purple = "\033[0;35m"


print(f"{red:^20}={white}={blue}=", end="")
print(f"{yellow} Music App ", end ="")
print(f"{blue}={white}={red}=\n")
print(f"🔥 ▶️ {white:<10}Radio Gaga")
print(f"{yellow:<15}Queen\n")
print(f"{white}PREV\n{green:<15}NEXT\n{purple:<22}PAUSE")
print("\n\n")


print(f"{white:^20}WELCOME TO\n{blue:<15}--", end ="")
print(f"{blue:<11} ARMBOOK{blue:<12}--")
print(f"\n{yellow:^16}Definetly not a rip off of\n{yellow:^19} a certain other social\n{yellow:^25} networking site.\n")
print(f"{red:^22}Honest.\n")
print(f"{white:^21}Username\n{white:^21}Pasword")