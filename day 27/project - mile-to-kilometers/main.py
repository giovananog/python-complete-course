from tkinter import *

window = Tk()
window.title("Miles to km convertor")
window.minsize(100, 80)
window.config(padx=2, pady=2)

def calc():
    km_label_anw["text"] = int(miles_input.get()) * 1,60934


miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

km_label_anw = Label(text=0)
km_label_anw.grid(column=1, row=1)

miles_input = Entry()
miles_input["text"] = 0
miles_input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(column=1, row=2)


window.mainloop()