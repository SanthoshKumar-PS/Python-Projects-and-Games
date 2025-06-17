import turtle
from turtle import Turtle,Screen
import random as rr

turtle.colormode(255)
def randomcolor():
    r=rr.randint(0,255)
    g=rr.randint(0,255)
    b=rr.randint(0,255)
    tup=(r,g,b)
    return tup

myturtle=Turtle()
currentheadind = myturtle.heading()
myturtle.speed("fastest")
for i in range(180):
    myturtle.color(randomcolor())
    myturtle.setheading(currentheadind)
    myturtle.circle(100)
    currentheadind+=2
screen=Screen()
screen.exitonclick()