from turtle import Turtle,Screen
import time
from mysnakeclass import Snake
from scoreboard import Score
from food import Food

screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
snake=Snake()
snake.createsnake()
screen.update()
food=Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
score=Score()

gameison=True
while gameison:
    screen.update()
    time.sleep(0.081)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extendsnake()
        score.clear()
        score.updatescore()
    if snake.head.xcor()>380 or snake.head.xcor()<-380 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.gameover()
        gameison=False

    for segment in snake.MYTURTLES_LIST:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.gameover()
            gameison = False
            

screen.exitonclick()

