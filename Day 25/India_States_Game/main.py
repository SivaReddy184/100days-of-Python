from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.addshape(image)
turtle = Turtle(image)

data = pandas.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/30 states correct", prompt="What's the state name?").\
        title()
    state_row = data[data["state"] == answer_state]
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_row.x), int(state_row.y))
        tim.write(answer_state)

screen.mainloop()

# Code to plot in images(.gif format)
# def get_mouse_click_corr(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_corr)
# turtle.mainloop()
