from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 278)
        self.displayscore()

    def displayscore(self):

        self.write(f"Score: {self.score}", False, "center", ("Arial", 12, "normal"))


    def gameover(self):
        self.goto(0,0)
        self.write("Game over",False,"center",("Arial",15,"normal"))

    def updatescore(self):
        self.score += 1
        self.write(f"Score: {self.score}", False, "center", ("Arial", 12, "normal"))