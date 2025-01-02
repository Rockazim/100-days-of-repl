"""There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff never washes out.

Regardless, your program today must:

Prompt the user to input the quantity and size of pizzas.

Multiply the two inputs together to calculate the cost of the pizzas.

Store that in a 2D list with the user's name.

Use try.... except for two reasons:

Include auto-save and auto-load. Use it with the auto-load.
When casting the quantity of pizzas to an integer. 
Avoid the user crashing the program by typing 'three'
 instead of '3'. Or any other non-integer input. If they do, then prompt them to try again."""

pizzas = []
try:
    f = open("pizza.txt", "r")
    pizzas = eval(f.read())
    f.close()
except:
    print("The file does not exist!")

def add():
    name = input("Name please: ").capitalize()
    toppings = input("Toppings: ").capitalize()
    size = input("Size (s/m/l): ")
    try:
        quantity = int(input("Quantity: "))
    except:
        print("Try again!\n")
        add()
    if size == "s":
        price = 4
    elif size == "m":
        price = 7
    elif size == "l":
        price = 10

    total = quantity * price
    pizzas.append([name, toppings, size, quantity, total])

def view():
    header = ["Name","Topping","Size","Quantity","Total"]
    print(f"{header[0]:^10}{header[1]:^10}{header[2]:^10}{header[3]:^10}{header[4]:^10}")
    for row in pizzas:
        for col in row:
            print(f"{col:^10}", end="")
        print()
    print()

while True:
    print("Azim's Pizza\n")
    try:
        main_menu = int(input("1: Add Pizza\n2: View Pizza\n>"))
    except:
        print("Please use an int!")
    if main_menu == 1:
        add()
    elif main_menu == 2:
        view()
    try:
        f1 = open("pizza.txt", "w")
        f1.write(str(pizzas))
        f1.close()
    except:
        print("This did not work!")