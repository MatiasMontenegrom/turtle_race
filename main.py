import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False


def create_turtle(tim, positions, color):
    tim = Turtle("turtle")
    tim.speed(500)
    all_turtles.append(tim)
    tim.hideturtle()
    tim.penup()
    tim.goto(-230, positions)
    tim.color(colors[color])
    tim.showturtle()


position = 150
for i in range(6):
    create_turtle("tim", position, i)
    position -= 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")
        random_distance = random.randint(1, 20)
        turtle.forward(random_distance)

screen.exitonclick()
