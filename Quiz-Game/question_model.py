# Question model which is used by the GUI to generate question text and options
class Question:

    def __init__(self, q_text, answer, options):
        self.text = q_text
        self.answer = answer
        self.options = options
