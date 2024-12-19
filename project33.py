"""Create your own to do list manager. (This can be super useful!)
Ask the user whether they want to view, add, or edit their to do list.
If they want to view it, print it out in a nice way (Hint: subroutine).
If they choose to add an item to the to do list, allow them to type in the item and then add it to the bottom of the list.
If they want to edit the to do list, ask them which item they completed, and remove it from the list.
Don't worry about duplicates!
The first item you put in the list should be the first item you remove.
Add a title, some color, alignment to the text, or emojis. Show off your skills!
Example:"""
green = "\033[0;32m"
red = "\033[0;31m"

ToDo = []

def printList(list):
    for x in list:
        
        print(x)

while True:
    print("\033[0;32m","ToDo List Manger", sep="")
    question = input(f"\n{green}Do you want to view, add, or edit your to do list? {red}\n")
    
    if question == "view":
        print()
        printList(ToDo)
        print()

    elif question == "add":
        AddToDo = input(f"\nWhat do you want to add {red}\n")
        ToDo.append(AddToDo)
        print()

    elif question == "edit":
        RemoveToDo = input(f"\n{green}What do you want to remove? {red}\n")
        print()
        if RemoveToDo in ToDo:
            ToDo.remove(RemoveToDo)
        else:
            print(f"{green}Doesn't exist!")
            continue
    else:
        print(f"{green}Try again!")
        continue

    