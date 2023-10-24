from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UI:
    def check(self, answer):
        if self.quiz.check_answer(answer): 
            self.score_text.config(text=(f"Score = {self.quiz.score}"))

    def true_f(self):
        if self.quiz.still_has_questions():
            self.check(True)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")


    def false_f(self):
        if self.quiz.still_has_questions():
            self.check(False)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas()

        self.score_text = Label(text="Score = 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="teste", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images\\false.png")
        false_img = PhotoImage(file="images\\true.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_f)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_f)
        self.false_button.grid(column=1, row=2)
        q_text = self.quiz.next_question()

        self.canvas.itemconfig(self.question_text, text=q_text)
        self.window.mainloop()
