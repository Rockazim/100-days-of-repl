#Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.

exit = ""

while exit != "yes":
    animal = input("What animal do you want?: ")
    if animal == "cow":
      print("A cow goes moo.")
    elif animal == "monkey":
      print("A monkey goes ooh ooh ah ah.")
    elif animal == "lion":
      print("A lion goes roar.")
    else:
      print("Try a different animal")
    exit = input("Do you want to exit?: ")