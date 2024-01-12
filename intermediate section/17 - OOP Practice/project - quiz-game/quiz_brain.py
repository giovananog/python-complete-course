class QuizBrain:
  
  def __init__(self, quiz_list):
    self.question_number = 0
    self.question_list = quiz_list
    self.score = 0

  
  def still_has_questions(self):
    return self.question_number < len(self.question_list)

  
  def check_answer(self, answer):
    if answer.title() == self.question_list[self.question_number].answer:
        print("You got it right! ")
        self.score += 1
    else:
        print("That's wrong! ")
    print(f"The correct answer was: {self.question_list[self.question_number].answer}\nYour current score is: ({self.score}/{self.question_number+1})")
    

  
  def next_question(self):  
    next = input(f"\n\nQ.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)? ")
    self.check_answer(next)
    self.question_number += 1
    