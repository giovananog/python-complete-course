from tkinter import*
from tkinter import messagebox
from random import *
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():

    # aqui tem q ter um exception para filenotfound!!
    with open("data.json","r") as data:
        content = json.load(data)
    try:
        dict_data = content[website_entry.get().title()]
    except KeyError:
        messagebox.showerror("Not found", "This website does not belong to the actual database")
    else:
        messagebox.showinfo(website_entry.get().title(), f"email: {dict_data['email']}, \n password: {dict_data['password']}")
       
# nesse caso um if e else seria suficiente para o keyerror, era só checar     if website_entry.get().title() in content

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

    new_data = {
       website_entry.get(): {
           "email": email_entry.get(),
           "password": psw_entry.get()
       }       
    }

    if website_entry.get() == "" or psw_entry.get() == "":
        messagebox.showinfo("error", "all the fields must be filled")
    else:
        with open("data.json", "r") as data:
            try:               
               # reading old data
               dataa = json.load(data)
            except:
               dataa = new_data
            else:
               # updating old data with new data
               dataa.update(new_data)
               
        with open("data.json", "w") as data:
            # saving updated data
            json.dump(dataa, data, indent=4)
        
        website_entry.delete(0, END)
        psw_entry.delete(0, END)
        messagebox.showinfo("yay!", "the information was saved!")
 


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
website_entry = Entry(width=20)
website_entry.grid(column=1 , row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0 , row=2)
email_entry = Entry(width=38)
email_entry.insert(0, "ongiovana2016@gmail.com")
email_entry.grid(column=1 , row=2, columnspan=2)

psw_label = Label(text="Password:")
psw_label.grid(column=0 , row=3)
psw_entry = Entry(width=20)
psw_entry.grid(column=1 , row=3)

generate_psw = Button(text="Generate Password", command=generate, width=14)
generate_psw.grid(row=3, column=2)

add_new = Button(text="Add", width=32, command=add_person)
add_new.grid(row=4, column=1, columnspan=2)

search_website = Button(text="Search", command=search, width=14)
search_website.grid(row=1, column=2, columnspan=1)

window.mainloop()