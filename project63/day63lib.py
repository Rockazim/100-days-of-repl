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