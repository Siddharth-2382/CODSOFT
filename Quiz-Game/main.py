from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Initialise an empty question bank
question_bank = []

# Iterate over question_data and generate question bank using Question class
for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]
    options = [correct_answer]
    options.extend(incorrect_answers)
    new_question = Question(question_text, correct_answer, options)
    question_bank.append(new_question)

# Create a QuizBrain object with a fresh question bank
quiz = QuizBrain(question_bank)

# Create a QuizInterface object with the quiz
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
