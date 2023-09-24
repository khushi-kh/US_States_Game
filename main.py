import pandas
import turtle
from scoreboard import ScoreBoard
import time

screen = turtle.Screen()
screen.bgpic("blank_states_img.gif")
screen.title("US STATE GAME")

t = turtle.Turtle()
t.hideturtle()
t.penup()

text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, 280)

scoreboard = ScoreBoard()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

user_name = screen.textinput(title="Your name", prompt="Enter your name").title()

while scoreboard.score != 50:
    text_turtle.clear()
    answer_state = screen.textinput(title=f"{scoreboard.score}/50 US States", prompt="Enter State").title()
    state_data = data[data.state == answer_state]

    if answer_state == "Exit":
        missed_states = pandas.DataFrame(all_states)
        missed_states.to_csv(f"{user_name}'s missed_states.csv")
        break

    if answer_state in all_states:
        x_cor = state_data.x.iloc[0]
        y_cor = state_data.y.iloc[0]

        t.goto(x_cor, y_cor)
        t.write(answer_state)
        scoreboard.increase_score()
        all_states.remove(answer_state)

    else:
        text_turtle.write("Wrong Input...Try Again", align="center", font=("Courier", 24, "bold"))
        time.sleep(0.8)
