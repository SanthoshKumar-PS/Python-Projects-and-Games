from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)



    def go_up(self):
        ycorr = self.ycor()
        self.goto(self.xcor(), ycorr + 10)

    def go_down(self):
        ycorr = self.ycor()
        self.goto(self.xcor(), ycorr - 10)

