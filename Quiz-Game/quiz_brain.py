import html


# Main Quiz Brain logic
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Check if there are any more questions left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Method to get the next question
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Format the data and unescape html formats
        q_text = html.unescape(self.current_question.text)
        q_options = self.current_question.options
        unescaped_options = []
        for option in q_options:
            unescaped_options.append(html.unescape(option))

        return {"question": f"Q.{self.question_number}: {q_text}",
                "options": unescaped_options}

    # Check if the answer selected by user is correct
    def check_answer(self, user_answer):
        correct_answer = html.unescape(self.current_question.answer)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
