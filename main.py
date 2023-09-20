from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def move_anticlock():
    tim.left(10)


def move_clock():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_anticlock, key="a")
screen.onkey(fun=move_clock, key="d")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
