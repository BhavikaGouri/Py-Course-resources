import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "US states/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

data = pandas.read_csv("US states/50_states.csv")
total_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"You Guessed {len(guessed_states)}/50", prompt="Write the name of State.")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in total_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_not_guessed.csv")
        break
    if answer_state in total_states:
        if answer_state in guessed_states:
            continue
        guessed_states.append(answer_state)
        state_name = data[data.state == answer_state]
        pen.goto(int(state_name.x), int(state_name.y))
        pen.write(answer_state,font=('Arial', 10, 'bold'))
