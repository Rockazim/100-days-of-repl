"""Your program should:

Create a backup folder.
Create a random filename.
Save a copy of the data to that file.
This should all happen before the auto save."""

import time, os, random

toDo = []

#you will need to comment this section out as no file will exist
try:
    f = open("toDo.txt", "r")
    toDo = eval(f.read())
    f.close()
except:
    print("ERROR: No existing to do list, using a blank list")


def add():
    print("ADD\n")
    q1 = input("What is it? ").capitalize()
    q2 = input("When is it due? ").capitalize()
    q3 = input("How important? ").capitalize()
    toDo.append([q1, q2, q3])


def priority(text):
    for x in toDo:
        for row in x:
            if text in x:
                print(f"{row:^10}", end=" | ")
        print()


def view():
    print("VIEW\n")
    q1 = int(input("1:View all\n2:View Priority\n"))
    if q1 == 1:
        for x in toDo:
            for row in x:
                print(f"{row:^10}", end=" | ")
            print()
    elif q1 == 2:
        prio = input("Which priority? ").capitalize()
        priority(prio)
    else:
        print("Wrong try Again! ")
        view()


def get_rid(trash):
    for x in toDo:
        if trash in x:
            toDo.remove(x)
    os.system("clear")
    print("Remove\n")
    for x in toDo:
        for row in x:
            print(f"{row:^10}", end=" | ")
        print()
    print("\n")
    time.sleep(3)


def edit():
    print("Edit\n")
    selection = input("What do you want to edit?\n").capitalize()
    time.sleep(2)
    os.system("clear")
    print("Edit\n")
    question1 = input("New title: ")
    question2 = input("New Due Date: ")
    question3 = input("New Priority: ")
    for x in range(len(toDo)):
        for y in range(len(toDo[x])):
            if toDo[x][y] == selection:
                toDo[x][0] = question1
                toDo[x][1] = question2
                toDo[x][2] = question3
    print("\nUpdated\n")


def backup():
    if "Backups" not in os.listdir():
        os.mkdir("Backups")
    random_nums = random.randint(1, 100)
    file_name = f"azim{random_nums}"
    access_file = os.path.join("Backups/", file_name)

    f2 = open(access_file, "w")
    f2.write(str(toDo))
    f2.close()


while True:
    question = int(
        input(
            "TODO List Management System \n\n1: Add\n2: View\n3: Remove\n4: Edit\n"
        ))
    time.sleep(2)
    if question == 1:
        os.system("clear")
        add()
        print("\nAdded to the list")
    elif question == 2:
        os.system("clear")
        view()
    elif question == 3:
        os.system("clear")
        print("Remove\n")
        removal = input("What would like to get rid of?\n").capitalize()
        get_rid(removal)
    elif question == 4:
        edit()
    else:
        print("Wrong try Again!\n")
        continue

    #Backup
    backup()

    f1 = open("toDo.txt", "w")
    f1.write(str(toDo))
    f1.close()
