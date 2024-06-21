from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick_marks = ""
check_mark = None
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="TIMER")
    check_mark.config(text="", bg=YELLOW)
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps > 9:
        return
    if reps % 8 == 0:
        text.config(text="BREAK",fg=RED)
        count_down(LONG_BREAK_MIN)
    elif reps % 2 == 0:
        text.config(text="BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        text.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global tick_marks, timer, check_mark
    minutes = math.floor(count/60)
    seconds = count % 60
    if len(str(seconds)) < 2:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_marks += "✔"
            check_mark = Label(text=tick_marks, bg=GREEN, font=("Arial", 20))
            check_mark.grid(row=3, column=1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

text = Label(text="TIMER", fg=PINK, bg=YELLOW, font=(FONT_NAME, 45, "normal"))
text.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="pomodoro-timer/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
