from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip
import json

# ----- search -------#
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(f"Error", f"{website}  Not Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(f"{website}  Found", f"website: {website}  mail:{email}  password: {password}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_information():
    website = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": mail,
            "password": password,
        }
    }

    if not (password and website and mail):
        messagebox.showerror("Error", "Please enter your website and password !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Would you like to save informations Email: {mail} password: {password} ")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #,


window = Tk()
window.title('Password Generator')
window.config(padx=51, pady=51)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row= 0 , column=1, columnspan=2)

#Labels
website_label = Label(text='Website:')
website_label.grid(row = 1, column = 0)
email_label = Label(text='Email:')
email_label.grid(row = 2, column = 0)
password_label = Label(text='Password:')
password_label.grid(row = 3, column = 0)

#Entries
website_entry = Entry(width = 35)
website_entry.grid(row = 1, column = 1,columnspan=2)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.insert(0, 'example@gmail.com')
email_entry.grid(row = 2, column = 1, columnspan=2)
password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

#Buttons
add_button = Button(text="Add", width=35, command=save_information)
add_button.grid(row = 4, column = 1, columnspan=2)
Generate_password = Button(text="Generate", command=generate_password)
Generate_password.grid(row = 3, column = 2)

search_button = Button(text= "Search", command=search)
search_button.grid(row = 1, column = 3)



window.mainloop()