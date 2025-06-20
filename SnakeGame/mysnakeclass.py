from turtle import Turtle

UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.MYPOSTIONS = [(0, 0), (-20, 0), (-40, 0)]
        self.MYTURTLES_LIST = []
        self.head=0

    def createsnake(self):
        for pos in self.MYPOSTIONS:
            self.addsnake(pos)

    def addsnake(self,pos):
        t1 = Turtle("square")
        t1.penup()
        t1.color("white")
        t1.goto(pos)
        self.MYTURTLES_LIST.append(t1)
        self.head = self.MYTURTLES_LIST[0]

    def extendsnake(self):
        self.addsnake(self.MYTURTLES_LIST[-1].position())

    def move(self):
        for num in range(len(self.MYTURTLES_LIST) - 1, 0, -1):
            xcor = self.MYTURTLES_LIST[num - 1].xcor()
            ycor = self.MYTURTLES_LIST[num - 1].ycor()
            self.MYTURTLES_LIST[num].goto(xcor, ycor)

        self.MYTURTLES_LIST[0].forward(20)


    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
