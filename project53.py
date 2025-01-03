"""Your video game inventory system should:

Have a menu that allows the user to:
Add
View
Remove
Adding an item saves it to a file using captalize mode. Duplicates are allowed.
Removing an item deletes it from the file.
View is trickier. It should output the name of the item and tell you how many of those items you have.
Use auto-save and auto-load with try... except."""


import time, os

inventory = []
try:
    f = open("inventory.txt", "r")
    inventory = eval(f.read())
    f.close()
except:
    print("File does not exist!")


def add():
    item = input("Item to add > ").capitalize()
    inventory.append(item)
    print("Added\n")
    time.sleep(2)
    os.system("clear")


def view():
    duplicates = []
    print("INVENTORY")
    print("=========\n")
    for x in inventory:
        count = inventory.count(x)
        if count == 1:
            print(f"{x} {count}")
        elif x not in duplicates:
            print(f"{x} {count}")
            duplicates.append(x)
        else:
            continue
    print()
    time.sleep(2)
    os.system("clear")


def remove():
    item_removed = input("Item to remove > ").capitalize()
    count = inventory.count(item_removed)
    if count > 1:
        try:
            user_choice = int(
                input(
                    f"Remove everything?\n1: Remove one {item_removed}\n2: Remove all {count}\n> "
                ))
        except:
            print("Please use an integer!")
            remove()
        if user_choice == 1:
            inventory.remove(item_removed)
        else:
            for x in range(count):
                inventory.remove(item_removed)

    elif count == 1:
        inventory.remove(item_removed)
    else:
        print("That doesn't exist")
        remove()
    time.sleep(2)
    os.system("clear")


while True:
    print("INVENTORY")
    print("=========\n")
    try:
        menu = int(input("1: Add\n2: View\n3: Remove\n> "))
    except:
        print("Please use an integer!")

    if menu == 1:
        add()
    elif menu == 2:
        view()
    elif menu == 3:
        remove()
    try:
        f1 = open("inventory.txt", "w")
        f1.write(str(inventory))
        f1.close()
    except:
        print("File does not exist!")
    time.sleep(2)
    os.system("clear")
