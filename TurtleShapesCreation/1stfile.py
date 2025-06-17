from turtle import Turtle,Screen

myturtle=Turtle()

for i in range(15):
    myturtle.forward(10)
    myturtle.penup()
    myturtle.forward(10)
    myturtle.pendown()

screen=Screen()
screen.exitonclick()
