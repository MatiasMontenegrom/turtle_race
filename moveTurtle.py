from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def back_wards():
    tim.backward(10)


def move_left():
    tim.left(5)


def move_right():
    tim.right(5)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkeypress(move_forwards, key="w")
screen.onkeypress(back_wards, key="s")
screen.onkeypress(move_left, key="a")
screen.onkeypress(move_right, key="d")
screen.onkeypress(clear, key="c")

screen.exitonclick()
