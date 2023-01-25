from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    entry3.delete(0, END)
    password = []
    for i in range(1, 21):
        rnd = random.randint(0, 2)
        if rnd == 0:
            password.append(random.choice(letters))
        elif rnd == 1:
            password.append(random.choice(numbers))
        else:
            password.append(random.choice(symbols))

    passwo = "".join(password)
    entry3.insert(0, passwo)
    pyperclip.copy(passwo)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file():
    web_ent = entry1.get()
    email_ent = entry2.get()
    password = entry3.get()

    new_data = {
        web_ent: {
            "email": email_ent,
            "password": password,
        }
    }

    if len(web_ent) == 0 or password == "":
        messagebox.showinfo(title="Oops", message="more data")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data

                data = json.load(data_file)
                # Update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        entry1.delete(0, END)
        entry3.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    web_ent = entry1.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if web_ent in data:
                email = data[web_ent]["email"]
                password = data[web_ent]["password"]
                messagebox.showinfo(title=web_ent, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title=web_ent, message="There is no site saved like that")
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="There is no data file found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry1 = Entry(window, width=42)
entry1.grid(column=1, row=1)
entry1.focus()

generate_button = Button(text="SEARCH", command=search, width=14)
generate_button.grid(column=2, row=1)

label_emus = Label(text="Email/Username:")
label_emus.grid(column=0, row=2)

entry2 = Entry(window)
entry2.config(width=60)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(0, "maniana@gmail.com")

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)

entry3 = Entry(window)
entry3.config(width=42)
entry3.grid(column=1, row=3)

generate_button = Button(text="Generate password", command=pass_generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=51, command=write_to_file)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
