from tkinter import*
from pandas import*
from random import*

current_card = None
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = (read_csv("data/words_to_learn.csv")).to_dict(orient="records")
except FileNotFoundError:
    data = (read_csv("data/french_words.csv")).to_dict(orient="records")


def next_card():
    global current_card
    global a
    window.after_cancel(a)
    current_card = choice(data)
    canvas.itemconfig(img, image=front_img)
    canvas.itemconfig(word, text=current_card["Portuguese"], fill="black")
    canvas.itemconfig(title, text="Português",)
    canvas.itemconfig(title, fill="black")
    a = window.after(3000, other_side)

    
def other_side():
    global current_card
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(title, text="Inglês")    
    

def save_word():
    data.remove(current_card)
    to_learn = DataFrame(data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    

def wrong_call():
    save_word()
    next_card()

window = Tk()
window.title("flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images\card_front.png")
back_img = PhotoImage(file="images\card_back.png")
img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images\\right.png")
right = Button(image=right_img, width=50, height=50, pady=15, command=next_card)
right.grid(column=1, row=1)

wrong_img = PhotoImage(file="images\\wrong.png")
wrong = Button(image=wrong_img, width=50, height=50, pady=15, command=wrong_call)
wrong.grid(column=0, row=1)


a = window.after(3000, other_side)
next_card()

window.mainloop()


