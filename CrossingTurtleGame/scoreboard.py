from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-220,250)
        self.updatelevel()

    def updatelevel(self):
        self.clear()
        self.write(f"Level: {self.level}",align="center",font=FONT)


    def levelup(self):
        self.level+=1
        self.updatelevel()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)



