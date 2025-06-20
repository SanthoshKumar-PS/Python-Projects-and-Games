from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xincrease=10
        self.yincrease=10
        self.speedo=0.1



    def move(self):
        self.goto(self.xcor()+self.xincrease,self.ycor()+self.yincrease)

    def bouncey(self):
        self.yincrease*=-1
        self.speedo*=0.9

    def bouncex(self):
        self.xincrease*=-1
        self.speedo*=0.9

    def reset_ball(self):
        self.goto(0,0)
        self.xincrease*=-1
        self.yincrease*=-1