from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip


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

    if not (password and website and mail):
        messagebox.showerror("Error", "Please enter your website and password !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Would you like to save informations Email: {mail} password: {password} ")
        if is_ok:
            with open("data.txt", "a") as file:
                data = f"{website} | {mail} | {password}\n"
                file.writelines(data)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
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
website_entry.grid(row = 1, column = 1, columnspan=2)
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



window.mainloop()