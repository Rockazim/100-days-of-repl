"""Build a really cool to do list manager. (I know we did this before...hold on!)

We are going to upgrade the last to do list manager we created:

Create a menu where the user can view, add, or remove an item.
The user should be able to edit the text of an item on the list too.
Don't allow the user to add duplicates.
Double check with the user they want to remove an item from the list before it is actually removed. (Is this the item they really want to remove?)
Give the user the option to completely erase the to do list. (You should be able to do this in one line of code!)
Example:

To Do List Manager:
Do you want to view, add, edit, or remove an item from the to do list?
view
record the video for day 36
Do you want to view, add, edit, or remove an item from the to do list?
remove
What do you want to remove?
record the video for day 36
Are you sure you want to remove this?
yes"""


toDo = []

#function for view
def view(list):
    for i in list:
        print(i)

def checkdupes(addition,list):
    for i in list:
        if i == addition:
            return True
    return False

def change(oldword,newword,list):
    for x in range(len(list)):
        if list[x] == oldword:
            list[x] = newword
    


while True:
    print("ToDo List Manager\n")
    question = input("Do you want to view, add, remove, or edit the todo list? \n")

    if question == "view":
        print("")
        view(toDo)
        print("")
        


    elif question == "add":
        addition = input("\nWhat do you want to add?\n") 
        if addition in toDo:
            print("Thats a duplicate try again!\n")
            continue
        else:
            print("")
            toDo.append(addition)

    elif question == "remove":
        remove = input("\nWhat do you want to remove?\n")
        if remove in toDo: 
            doublecheck = input("\nAre ya sure? (Y/N): ")
            if doublecheck == "Y":
                toDo.remove(remove)
        else:
            print("\nSorry but that doesn't exist!")

        deleteList = input("\nWould you like to delete the whole list(Y/N): \n")
        if deleteList == "Y":
            toDo = []
                            
    elif question == "edit":
        edit = input("\nWhat do you want to edit?\n")
        if edit in toDo:
            newword = input("\nPlease provide the new word!\n")
            change(edit, newword, toDo)
            print("")
        else:
            print("That word doesn't exist!")
    else:
        continue
        