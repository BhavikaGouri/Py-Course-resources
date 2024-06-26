from tkinter import *
import pandas
import random

question = None

learnt_words = []
data = pandas.read_csv("spanish-flash-cards/spanish_words.csv")
data_dict = {row["Spanish"]: row["English"] for (index, row) in data.iterrows()}
spanish_words = data["Spanish"].to_list()


def new_word():
    global question
    question = random.choice(spanish_words)
    spanish_words.remove(question)
    canvas.itemconfig(screen, image=card_front)
    canvas.itemconfig(title, text="Spanish", font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(word, text=question, fill="black")
    canvas.after(3000, func=answer)


def answer():
    global question
    canvas.itemconfig(screen, image=card_back)
    canvas.itemconfig(title, text="English", font=("Ariel", 40, "italic"), fill="blue")
    canvas.itemconfig(word, text=data_dict[question], fill="blue")


def learnt():
    learnt_words.append(question)
    learnt_data = pandas.Series(learnt_words)
    learnt_data.to_csv("./data/known_words.csv")
    window.after(200, new_word)


# ------------------ UI SETUP --------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCARDS")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="spanish-flash-cards/card_front.png")
card_back = PhotoImage(file="spanish-flash-cards/card_back.png")
screen = canvas.create_image(400, 263, image=card_front)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="spanish-flash-cards/wrong.png")
wrong_button = Button(image=wrong, highlightbackground=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="spanish-flash-cards/right.png")
right_button = Button(image=right, highlightbackground=BACKGROUND_COLOR, command=learnt)
right_button.grid(row=1, column=1)

new_word()
window.mainloop()
