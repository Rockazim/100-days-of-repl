"""Today, you're going to program a full on Mokébeast Mokédex. Yep, think we're getting away with it so far...

Don't forget, you can reuse your code from Day 42 here.

Your Mokédex should:

Store multiple Mokébeasts using a loop.
Get user input of the beasts' details.
Add the details to a 2D dictionary.
Repeat until the user wants to stop.
Output the full Mokédex using a prettyPrint() function.
Example:"""


mokébeast = {"name" : None, "type" : None, "special move" : None, "starting HP" : None, "starting MP" : None}
mokédex = {}

def generate():
    for i, x in mokébeast.items():
        mokébeast[i] = input(f"Input your beast's {i} > ").capitalize().strip()
        
    mokédex[mokébeast["name"]] = {"name" : mokébeast["name"], "type" : mokébeast["type"], "special move" : mokébeast["special move"], "starting HP" : mokébeast["starting HP"], "starting MP" : mokébeast["starting MP"]}

def prettyprint():
    for key, value in mokédex.items():
        for subkey, subvalue in value.items():
            print(f"{subkey:^10}: {subvalue:^10}", end=" | ")
        print()


while True:
    generate()
    prettyprint()
    again = input("Again? (Y/N)? ").capitalize().strip()
    
    if again == "Y":
        continue
    else:
        prettyprint()
        break