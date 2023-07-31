from tkinter import *
import random

# Define constants
RED = "#e7305b"
PURPLE = "#9000a0"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"


# Logic for generating password
def generate_password():
    pass


# GUI using tkinter
window = Tk()

# Label for the title
title_label = Label(text="Welcome To Password Generator!", bg=YELLOW, fg=PURPLE, font=(FONT_NAME, 45))
title_label.pack()

# Label for Number of Letters
letter_label = Label(text="1. How many letters would you like in your password?", bg=YELLOW, fg=BLACK, font=(FONT_NAME,
                                                                                                             20))
letter_label.place(x=10, y=100)

# Spinbox for Number of Letters
letter_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
letter_input.place(x=675, y=100)

# Label for Number of Symbols
symbols_label = Label(text="2. How many symbols would you like?", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 20))
symbols_label.place(x=10, y=150)

# Spinbox for Number of Symbols
symbols_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
symbols_input.place(x=675, y=150)

# Label for Number of Numbers
number_label = Label(text="3. How many numbers would you like?", bg=YELLOW, fg=BLACK, font=(FONT_NAME, 20))
number_label.place(x=10, y=200)

# Spinbox for Number of Numbers
number_input = Spinbox(from_=0, to=20, width=10, font=(FONT_NAME, 20))
number_input.place(x=675, y=200)

# Button for Generating Password
generate_button = Button(text="Generate", bg=PURPLE, font=(FONT_NAME, 20), command=generate_password)
generate_button.pack(pady=200)

# Field for the Generated Password
password_field = Entry(width=42, font=(FONT_NAME, 30), fg=RED)
password_field.place(x=10, y=350)

# Screen configurations
window.title("Password Generator App")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("+270+100")
window.minsize(width=270, height=300)
window.resizable(False, False)

window.mainloop()
