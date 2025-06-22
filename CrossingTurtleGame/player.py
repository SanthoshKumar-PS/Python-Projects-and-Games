from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.resetplay()

    def go_up(self):
        self.forward(20)

    def isatfinishline(self):
        if self.ycor()>=280:
            return True
        else:
            return False

    def resetplay(self):
        self.goto(STARTING_POSITION)