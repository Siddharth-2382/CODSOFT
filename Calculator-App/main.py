from tkinter import *

# Constants
THEME_COLOR = "#FFF6DC"
FONT_NAME = "Courier"


# Function to handle button press for expression values
def press(x):
    pass


def clear():
    input_entry.delete(0, END)


def evaluate():
    pass


window = Tk()

# Entry field for input
input_entry = Entry(font=(FONT_NAME, 25))
input_entry.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

# Buttons for numbers
b0 = Button(text="0", height=1, width=2, font=(FONT_NAME, 25), command=press(0))
b0.grid(row=4, column=0, pady=15)

b1 = Button(text="1", height=1, width=2, font=(FONT_NAME, 25), command=press(1))
b1.grid(row=3, column=0, pady=15)

b2 = Button(text="2", height=1, width=2, font=(FONT_NAME, 25), command=press(2))
b2.grid(row=3, column=1, pady=15)

b3 = Button(text="3", height=1, width=2, font=(FONT_NAME, 25), command=press(3))
b3.grid(row=3, column=2, pady=15)

b4 = Button(text="4", height=1, width=2, font=(FONT_NAME, 25), command=press(4))
b4.grid(row=2, column=0, pady=15)

b5 = Button(text="5", height=1, width=2, font=(FONT_NAME, 25), command=press(5))
b5.grid(row=2, column=1, pady=15)

b6 = Button(text="6", height=1, width=2, font=(FONT_NAME, 25), command=press(6))
b6.grid(row=2, column=2, pady=15)

b7 = Button(text="7", height=1, width=2, font=(FONT_NAME, 25), command=press(7))
b7.grid(row=1, column=0, pady=15)

b8 = Button(text="8", height=1, width=2, font=(FONT_NAME, 25), command=press(8))
b8.grid(row=1, column=1, pady=15)

b9 = Button(text="9", height=1, width=2, font=(FONT_NAME, 25), command=press(9))
b9.grid(row=1, column=2, pady=15)

# Buttons for different functions
clear_btn = Button(text="CLEAR", height=1, width=18, font=(FONT_NAME, 25), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=15)

divide = Button(text="/", height=1, width=2, font=(FONT_NAME, 25), command=press("/"))
divide.grid(row=1, column=3)

multiply = Button(text="*", height=1, width=2, font=(FONT_NAME, 25), command=press("*"))
multiply.grid(row=2, column=3)

addition = Button(text="+", height=1, width=2, font=(FONT_NAME, 25), command=press("+"))
addition.grid(row=3, column=3)

subtract = Button(text="-", height=1, width=2, font=(FONT_NAME, 25), command=press("-"))
subtract.grid(row=4, column=3)

equal = Button(text="=", height=1, width=2, font=(FONT_NAME, 25), command=evaluate)
equal.grid(row=4, column=2)

point = Button(text=".", height=1, width=2, font=(FONT_NAME, 25), command=press("."))
point.grid(row=4, column=1)

# Window configuration
window.title("Calculator")
window.config(padx=20, pady=20, bg=THEME_COLOR)
window.geometry("+575+125")
window.minsize(width=325, height=500)
window.resizable(False, False)
window.mainloop()
