from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]

    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
          "email": email,
          "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
            messagebox.showinfo(title="oops", message="One of the fields are empty, please fill all the details!")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=2)
                password_entry.delete(0, "end")
                website_entry.delete(0, "end")
        else:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=2)
                password_entry.delete(0, "end")
                website_entry.delete(0, "end")


# ---------------------------- SEARCH ------------------------------- #


def search():
    try:
        with open("data.json", "r") as f:
            search_data = json.load(f)
            search_entry = website_entry.get()
            list_data = list(search_data)
            if website_entry.get() in list_data:
                messagebox.showinfo(title=f"{search_entry}", message=f"Email: {search_data[search_entry]['email']} \n"
                                                                     f"Password: {search_data[search_entry]['password']}")
            else:
                messagebox.showinfo(title=f"{search_entry}", message=f"No Data for {search_entry}")

    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, height=220, width=220)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=19)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "omersella95@gmail.com")

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=10, command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(column=2, row=1)


window.mainloop()
