# Turtle Race
from turtle import Turtle, Screen
import random

screen = Screen()
race_on = False
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
screen.setup(width=500, height=400)

y_cor = [-100, -70, -40, -10, 20, 50]
turtle_list = []

for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_cor[index])
    turtle_list.append(tim)

player_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if player_bet:
    race_on = True

while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_on = False
            if player_bet == winner:
                print(f"You won! The {winner} turtle won the race!")
            else:
                print(f"You Lost. The {winner} turtle won the race!")
        dist = random.randint(0, 10)
        turtle.forward(dist)


screen.exitonclick()
