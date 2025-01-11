"""Your challenge is to create a simple GUI calculator.

Your program should:

Have buttons for the numbers 0 to 9, plus, minus, multiply, divide and equals.
The user should be able to press buttons to create their calculation.
It should output the correct result when they press equals."""

import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("700x500")

label = ""


def updateLabel(new_label):
    global label
    label += new_label
    hello["text"] = label


def calculate():
    global label
    number1 = ""
    number2 = ""
    sign = ""
    for x in range(len(label)):
        if label[x] == "+" or label[x] == "*" or label[x] == "/" or label[x] == "-":
            sign = label[x]
            number1 = label[0:x]
            number2 = label[x + 1:len(label)]
    number1 = float(number1)
    number2 = float(number2)  
    expression = f"{number1} {sign} {number2}"
    expression = eval(expression)
    label = str(expression)
    hello["text"] = label

def clear():
    global label
    label = ""
    hello["text"] = label

hello = tk.Label(text=label)
hello.grid(row=0, column=10)


button1 = tk.Button(text="1", command=lambda: updateLabel("1"),).grid(row=2, column=3)
button2 = tk.Button(text="2", command=lambda: updateLabel("2")).grid(row=2, column=4)
button3 = tk.Button(text="3", command=lambda: updateLabel("3")).grid(row=2, column=5)
addition = tk.Button(text="+", command=lambda: updateLabel("+")).grid(row=2, column=6)
subtraction = tk.Button(text="-", command=lambda: updateLabel("-")).grid(row=2, column=7)

button4 = tk.Button(text="4", command=lambda: updateLabel("4")).grid(row=3, column=3)
button5 = tk.Button(text="5", command=lambda: updateLabel("5")).grid(row=3, column=4)
button6 = tk.Button(text="6", command=lambda: updateLabel("6")).grid(row=3, column=5)
multiplication = tk.Button(text="*", command=lambda: updateLabel("*")).grid(row=3, column=6)
division = tk.Button(text="/", command=lambda: updateLabel("/")).grid(row=3, column=7)

button7 = tk.Button(text="7", command=lambda: updateLabel("7")).grid(row=4, column=3)
button8 = tk.Button(text="8", command=lambda: updateLabel("8")).grid(row=4, column=4)
button9 = tk.Button(text="9", command=lambda: updateLabel("9")).grid(row=4, column=5)
button0 = tk.Button(text="0", command=lambda: updateLabel("0")).grid(row=5, column=4)
equals = tk.Button(text="=", command=calculate).grid(row=5, column=6)
get_rid = tk.Button(text="C", command=clear).grid(row=5, column=7)

tk.mainloop()
