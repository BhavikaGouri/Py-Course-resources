from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("QUIZ")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.score}",
                                 fg="white",
                                 bg=THEME_COLOR,
                                 font=("Ariel", 20, "italic"))

        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=400, height=300)
        self.text = self.canvas.create_text(200,
                                            150,
                                            text="",
                                            width=380,
                                            fill="white",
                                            font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.RIGHT = PhotoImage(file="tkinter project quiz/true.png")
        self.LEFT = PhotoImage(file="tkinter project quiz/false.png")

        self.right = Button(image=self.RIGHT, highlightbackground=THEME_COLOR, command=self.right_pressed)
        self.right.grid(row=2, column=0)
        self.left = Button(image=self.LEFT, highlightbackground=THEME_COLOR, command=self.wrong_pressed)
        self.left.grid(row=2, column=1)
        self.next()
        self.window.mainloop()

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques = self.quiz.next_question()
            self.canvas.itemconfig(self.text,
                                   text=ques,
                                   fill="black",
                                   font=("Arial", 20, "italic"))
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of quiz")
            self.right.config(state="disabled")
            self.left.config(state="disabled")

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.update_screen(is_right)

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.update_screen(is_right)

    def update_screen(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.window.after(1500, self.refresh)
        else:
            self.canvas.config(bg="red")
            self.window.after(1500, self.refresh)

    def refresh(self):
        self.score_label.config(text=f"Score :{self.score}", font=("Ariel", 20, "italic"))
        self.next()

