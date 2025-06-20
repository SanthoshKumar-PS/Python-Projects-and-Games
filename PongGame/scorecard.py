from turtle import Turtle



class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.lscore=0
        self.rscore=0
        self.goto(0,230)
        self.hideturtle()
        self.color("white")
        self.updatescore_all()

    def updatescore_all(self):
        self.clear()
        self.write(f"{self.lscore} : {self.rscore}",align="center",font=("Comic Sans MS", 40, "normal"))

    def right_score(self):
        self.rscore+=1
        self.updatescore_all()

    def left_score(self):
        self.lscore+=1
        self.updatescore_all()

