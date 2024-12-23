"""Some trainers have no fear. To them, this is just one more challenge".

Create a dictionary to store the details of your, ahem, MokéBeast.
Ask the user to input the following details: name, type (earth, fire, air, water or spirit), special move, starting HP and starting MP. For now we're just taking in one set of values for one beast.
Output the beast's details.
Check the beast's type and change the color of the text accordingly. Fire is red, water is blue, air is white. You decide on the others."""

mokébeast = {"name" : None, "type" : None, "special move" : None, "starting HP" : None, "starting MP" : None}

def colorPrint(color, word):
    for i, x in word.items():
        if color == "red":
            print(f"\033[0;31m{i}: {x:^15}")
        elif color == "blue":
            print(f"\033[0;34m{i}: {x:^15}")
        elif color == "yellow":
            print(f"\033[1;33m{i}: {x:^15}")
        elif color == "green":
            print(f"\033[0;32m{i}: {x:^15}")
        elif color == "brown":
            print(f"\033[0;33m{i}: {x:^15}")
        


for i, x in mokébeast.items():
    mokébeast[i] = input(f"Input your beast's {i} > ").capitalize().strip()

print()
if mokébeast["type"] == "Fire":
    colorPrint("red", mokébeast)
elif mokébeast["type"] == "Water":
    colorPrint("blue", mokébeast)
elif mokébeast["type"] == "Electric":
    colorPrint("yellow", mokébeast)
elif mokébeast["type"] == "Grass":
    colorPrint("green", mokébeast)
elif mokébeast["type"] == "Earth":
    colorPrint("brown", mokébeast)
