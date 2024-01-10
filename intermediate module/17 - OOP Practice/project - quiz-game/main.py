from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questions = []

for i in question_data:
  text = i["question"]
  answer = i["correct_answer"]
  new_question = Question(text, answer)
  questions.append(new_question)

quiz_brain = QuizBrain(questions)

while quiz_brain.still_has_questions():
   quiz_brain.next_question()

print("\n\nYou've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")