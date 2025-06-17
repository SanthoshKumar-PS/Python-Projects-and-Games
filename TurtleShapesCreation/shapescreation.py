from random import choice
from turtle import Turtle,Screen
import random
myturtle=Turtle()
myturtle.left(180)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

n=3
for i in range(5):
    for j in range(n):
        myturtle.forward(100)
        myturtle.left(360/n)
    n+=1
    myturtle.color(choice(colours))






screen=Screen()
screen.exitonclick()