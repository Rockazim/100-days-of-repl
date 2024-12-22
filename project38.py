"""Ask the user to input any sentence (string).
Now we'll rainbow-ize (nope, me neither) it.
As soon as the string contains an 'r', every letter from that point on should be red.
When the computer encounters a 'b', 'g', 'p' or 'y', from there the output should be blue for 'b', green for 'g'...you get the idea.
Loop through the string and output it (so the color continues through the loop).
The output should change color every time it encounters a new r,g,b,p or y.
🥳 Extra points for resetting the output color back to default every time there's a space."""

sentence = f"\033[1;33m{"What sentence do you want rainbow-isting"}"
green ="\033[0;32m"
blue ="\033[1;34m"
orange = "\033[38;2;255;165;0m"
yellow = "\033[1;33m"
indigo = "\033[0;34m"
violet = "\033[0;35m"
red = "\033[0;31m"
normal = "\033[1;37m"

question = input(f"{sentence}\n{green}")

for x in question:
    if x.lower() == "r":
        print(f"{red}{x}", end = "")
    elif x.lower() == "o":
        print(f"{orange}{x}", end = "")
    elif x.lower() == "y":
        print(f"{yellow}{x}", end = "")
    elif x.lower() == "g":
        print(f"{green}{x}", end = "")
    elif x.lower() == "b":
        print(f"{blue}{x}", end = "")
    elif x.lower() == "i":
        print(f"{indigo}{x}", end = "")
    elif x.lower() == "v":
        print(f"{violet}{x}", end = "")
    elif x == " ":
        print(f"{normal}{x}", end = "")
    else:
        print(x, end ="")    

        