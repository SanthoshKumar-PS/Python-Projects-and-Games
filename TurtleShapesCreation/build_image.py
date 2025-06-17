import turtle as t
import random

mycolors=[(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]
t.colormode(255)
myturtle=t.Turtle()
myturtle.shape("classic")
myturtle.speed("fastest")
myturtle.penup()
myturtle.setheading(225)
myturtle.forward(300)
for j in range(10):
    myturtle.setheading(0)
    for i in range(10):
        myturtle.pendown()
        myturtle.dot(20,random.choice(mycolors))
        myturtle.penup()
        myturtle.forward(50)
    myturtle.setheading(90)
    myturtle.forward(50)
    myturtle.setheading(180)
    myturtle.forward(500)



screen=t.Screen()
screen.exitonclick()