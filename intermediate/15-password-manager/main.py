from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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
    password_input.insert(0, password)


def find_password():
    website = website_input.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("File Not Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"Website: {website}", message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Website Not Found", message=f"No data for the Website: {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password = password_input.get()
    email = email_input.get()
    website = website_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(email) < 8 or len(password) < 8:
        messagebox.showerror(title="Invalid Entries",
                             message=f"Doesn't meet the requirements:\n Minimum Email: 8 Characters.\nMinimum Password: 8 Characters. ")
    else:
        is_ok = messagebox.askokcancel(title="Check Entries", message=f"These are the details entered: \nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}")
        if is_ok:
            try:
                with open("passwords.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=20)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
