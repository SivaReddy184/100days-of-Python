from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list_1 = [choice(letters) for char in range(randint(8, 10))]
    password_list_2 = [choice(symbols) for i in range(randint(2, 4))]
    password_list_3 = [choice(numbers) for j in range(randint(2, 4))]

    password_list = password_list_1 + password_list_2 + password_list_3
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    # pyperclip is a module which can copy the selected variable to clipboard
    pyperclip.copy(password)
    password_entry.insert(0, pyperclip.paste())
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get().lower()
    user = username_entry.get()
    paasword = password_entry.get()
    new_data = {
        web: {
            "email": user,
            "password": paasword
        }
    }
    with open("data.json") as data_file:
        website_data = json.load(data_file)
    if len(web) == 0 or len(paasword) == 0:
        messagebox.showwarning(title="OOPS", message="Hey don't leave your fields empty")
    elif web in website_data:
        messagebox.showwarning(title="Caution", message=f"You already saved {web} password, please use search button")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------------SEARCH FUNCTION-------------------------#
def search():
    searched_website = website_entry.get().lower()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="You are yet to save a password")
    else:
        if searched_website in data:
            email = data[searched_website]["email"]
            password = data[searched_website]["password"]
            messagebox.showinfo(title=searched_website.title(), message=f"Email: {email}\n Password: {password}\n")
        else:
            messagebox.showwarning(title="OOPS", message=f"You didn't saved {searched_website} website password")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label()
website_label.config(text="Website:", fg="black", font="bold")
website_label.grid(row=1, column=0)

username_label = Label()
username_label.config(text="Username/Email:", fg="black", font="bold")
username_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:", fg="black", font="bold")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_entry = Entry(width=54)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, string="sivasatish780@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
