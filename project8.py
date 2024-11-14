#Affirmations Generator

print("Positivity Machine")

name = input("What is your name? ")
day_of_week = input("What day of the week is it? ")
favorite_thing = input("What is your favorite thing to do?")
favorite_food = input("What is your favorite food?")
best_friend = input("Who is your best friend?")

if day_of_week == "Monday" or day_of_week == "monday":

  if name == "Josh" or name == "josh":
    print("Hey", name , "since its Monday go out and eat some", favorite_food, "and then go", favorite_thing, "with", best_friend)
  elif name == "Agatha" or name == "agatha":  
    print("Hey", name, "you're doing great! Don't forget to call",best_friend)
  else:
    print("That person doesn't exist")
elif day_of_week == "Tuesday" or day_of_week == "tuesday": 
  if name == "Josh" or name == "josh":
    print("Remember to eat", favorite_food, "today!!")
  elif name == "Agatha" or name == "agatha":  
    print("Feeling down? The go", favorite_thing, ":)")
  else:
    print("That person doesn't exist")

elif day_of_week == "Wednesday" or day_of_week == "wednesday":
  if name == "Josh" or name == "josh":
    print("Everyone loves you", name)
  elif name == "Agatha" or name == "agatha":  
    print("The world loves you", name)
  else:
    print("That person doesn't exist")
    
elif day_of_week == "Thursday" or day_of_week == "thursday": 
  if name == "Josh" or name == "josh":
    print("Be grateful for", best_friend)
  elif name == "Agatha" or name == "agatha":  
    print(best_friend, "is grateful for you :)")
  else:
    print("That person doesn't exist")

elif day_of_week == "Friday" or day_of_week == "friday": 
  if name == "Josh" or name == "josh":
    print("You're doing great", name)
  elif name == "Agatha" or name == "agatha":  
    print("Keep working hard", name)
  else:
    print("That person doesn't exist")

elif day_of_week == "Saturday" or day_of_week == "saturday":
  if name == "Josh" or name == "josh":
    print("lets go! it's", day_of_week, "spend some time doing", favorite_thing)
  elif name == "Agatha" or name == "agatha":  
    print("What day is it? It's your happy day", name)
  else:
    print("That person doesn't exist")

elif day_of_week == "Sunday" or day_of_week == "sunday":
  if name == "Josh" or name == "josh":
    print("Stay positive for the future")
  elif name == "Agatha" or name == "agatha":  
    print("Learn and move on from the past")
  else:
    print("That person doesn't exist")

else:
 print("Last time I checked, that's not a day of the week!! Try again!") 