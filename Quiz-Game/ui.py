from tkinter import *
import random
from quiz_brain import QuizBrain

# Constant for theme color of Quiz Game App
THEME_COLOR = "#375362"


# Class for Quiz GUI using Tkinter
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Setup GUI window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.geometry("+600+100")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas for questions
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some text here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons for multiple choice options
        self.option_1 = Button(text="Option 1", width=30, pady=5, command=self.option_1_pressed)
        self.option_1.grid(row=2, column=0, columnspan=2)

        # Spacer label
        self.label1 = Label(text="", bg=THEME_COLOR)
        self.label1.grid(row=3, column=0)

        self.option_2 = Button(text="Option 2", width=30, pady=5, command=self.option_2_pressed)
        self.option_2.grid(row=4, column=0, columnspan=2)

        # Spacer label
        self.label2 = Label(text="", bg=THEME_COLOR)
        self.label2.grid(row=5, column=0)

        self.option_3 = Button(text="Option 3", width=30, pady=5, command=self.option_3_pressed)
        self.option_3.grid(row=6, column=0, columnspan=2)

        # Spacer label
        self.label3 = Label(text="", bg=THEME_COLOR)
        self.label3.grid(row=7, column=0)

        self.option_4 = Button(text="Option 4", width=30, pady=5, command=self.option_4_pressed)
        self.option_4.grid(row=8, column=0, columnspan=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            # Update score
            self.score_label.config(text=f"score: {self.quiz.score}")

            # Get next question dictionary
            q_dict = self.quiz.next_question()
            q_text = q_dict["question"]
            q_options = q_dict["options"]

            # Shuffle the options randomly
            random.shuffle(q_options)

            # Update the canvas and buttons
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.option_1.config(text=q_options[0])
            self.option_2.config(text=q_options[1])
            self.option_3.config(text=q_options[2])
            self.option_4.config(text=q_options[3])
        else:
            self.score_label.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.option_1.config(state="disabled")
            self.option_2.config(state="disabled")
            self.option_3.config(state="disabled")
            self.option_4.config(state="disabled")

    # Handle button press

    def option_1_pressed(self):
        user_answer = self.option_1.cget('text')
        self.give_feedback(self.quiz.check_answer(user_answer))

    def option_2_pressed(self):
        user_answer = self.option_2.cget('text')
        self.give_feedback(self.quiz.check_answer(user_answer))

    def option_3_pressed(self):
        user_answer = self.option_3.cget('text')
        self.give_feedback(self.quiz.check_answer(user_answer))

    def option_4_pressed(self):
        user_answer = self.option_4.cget('text')
        self.give_feedback(self.quiz.check_answer(user_answer))

    # Flash green if correct otherwise flash red
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
