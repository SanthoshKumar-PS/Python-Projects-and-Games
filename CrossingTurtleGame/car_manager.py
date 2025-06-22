import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.carslist=[]
        self.normalspeed=STARTING_MOVE_DISTANCE


    def createcar(self):
        random_num=random.randint(1,6)
        if random_num==1:
            car=Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            car.goto(300,random_y)
            self.carslist.append(car)



    def movecar(self):
        for car in self.carslist:
            car.backward(self.normalspeed)

    def speeding(self):
        self.normalspeed +=MOVE_INCREMENT
