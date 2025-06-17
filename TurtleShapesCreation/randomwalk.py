import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
def turn(num):
    if num==0:
        myturtle.left(90)
        myturtle.forward(20)
    elif num==1:
        myturtle.right(90)
        myturtle.forward(20)
    elif num==2:
        myturtle.forward(20)
    elif num==3:
        myturtle.left(180)
        myturtle.forward(20)



myturtle=Turtle()
myturtle.pensize(10)
myturtle.speed(1000)
ran=[0,1,2,3]
colorsl=['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro']

i=0
while i<50:
    #if -300<myturtle.xcor()<300 and -300<myturtle.ycor()<300:
    # myturtle.color(random.choice(colorsl))
    myturtle.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

    turn(random.choice(ran))
    i+=1










screen=Screen()
screen.exitonclick()