from tkinter import*
from tkinter import messagebox
from random import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_list = []
    

    password_list += ([choice(letters) for _ in range(randint(8, 10))])
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])
    
    shuffle(password_list)
    
    password = "".join(password_list)
    
    psw_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_person():
    if website_entry.get() == "" or email_entry.get() == "" or psw_entry.get() == "":
        messagebox.showinfo("error", "all the fields must be filled")
    else:
        option = messagebox.askyesno("add new account", "data aproved, do you want to save this new account?")
        if option:
           dict = {}
           dict["website"] = website_entry.get()
           dict["email/username"] = email_entry.get()
           dict["password"] = psw_entry.get()
           with open("data.txt", "a") as data:
              data.write(str(dict) + "\n")
           website_entry.delete(0, END)
           psw_entry.delete(0, END)
           messagebox.showinfo("ok!", "the account was created!")
        else:
            messagebox.showwarning("...", "the account was not created.")


# ---------------------------- UI SETUP ------------------------------- #4


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=180, height=180, highlightthickness=0)
psw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=psw_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0 , row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1 , row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0 , row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "ongiovana2016@gmail.com")
email_entry.grid(column=1 , row=2, columnspan=2)

psw_label = Label(text="Password:")
psw_label.grid(column=0 , row=3)
psw_entry = Entry(width=20)
psw_entry.grid(column=1 , row=3)

generate_psw = Button(text="Generate Password", command=generate)
generate_psw.grid(row=3, column=2)

add_new = Button(text="Add", width=36, command=add_person)
add_new.grid(row=4, column=1, columnspan=2)


window.mainloop()