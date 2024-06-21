import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_generator():
    nr_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = nr_numbers + nr_symbols + nr_letters

    random.shuffle(password_list)
    password = "".join(password_list)

    text3_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = text1_input.get()
    email = text2_input.get()
    text_input = text3_input.get()

    if len(website) == 0 or len(email) == 0 or len(text_input) == 0:
        messagebox.showinfo(title="Error", message="Fields must not left empty.")
    else:
        confirm = messagebox.askokcancel(title=website,
                                         message=f"Your details:\nEmail:{email}\nPassword:"
                                         f"{text_input}\nis it okay?")
        new_data = {
            website: {
                "email": email,
                "password": text_input
            }
        }
        if confirm:

            try:
                with open("pass.json", "r") as file:
                    # json.dump(new_data, file, indent=4)
                    # file.write(f"{website} | {email} | {text_input}\n")
                    data = json.load(file)
            except FileNotFoundError:
                with open("pass.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("pass.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                text1_input.delete(0, END)
                text2_input.delete(0, END)
                text3_input.delete(0, END)

# ------------------------ SEARCH WEBSITE --------------------------------- #


def search():
    website = text1_input.get()
    if len(website) == 0:
        messagebox.showwarning(title="Incomplete prompt", message="Enter the website to search")
    else:
        try:
            with open("pass.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            messagebox.showinfo(title=website, message="File not found")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"email: {data[website]["email"]}\n"
                                                           f"password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title=website, message=f"Website named {website} is not found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Personal Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

text1 = Label(text="Website:")
text1.grid(row=1, column=0)

text2 = Label(text="Email/Username:")
text2.grid(row=2, column=0)

text3 = Label(text="Password:")
text3.grid(row=3, column=0)

text1_input = Entry(width=21)
text1_input.grid(row=1, column=1)
text1_input.focus()

text2_input = Entry(width=38)
text2_input.grid(row=2, column=1, columnspan=2)

text3_input = Entry(width=21)
text3_input.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=pass_generator)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1,column=2)
window.mainloop()
