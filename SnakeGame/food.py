from random import random
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        xcor=random.randint(-380,380)
        ycor=random.randint(-280,280)
        self.goto(xcor,ycor)


















