import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

screen=Screen()
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
right_paddle=Paddle((380,0))
left_paddle=Paddle((-380,0))

ball=Ball()
scorecard=Scorecard()



screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")



game_is_on=True
while game_is_on:
    screen.update()
    # to increase speed step by step time.sleep(ball.speedo)
    time.sleep(0.1)
    ball.move()
    if ball.ycor()>=290 or ball.ycor()<=-290:
        ball.bouncey()

    if ball.xcor()>=360 and ball.distance(right_paddle)<=50 or ball.xcor()<=-360 and ball.distance(left_paddle)<=50:
        ball.bouncex()

    if ball.xcor()>=390 :
        ball.reset_ball()
        scorecard.left_score()

    if ball.xcor()<=-390:
        ball.reset_ball()
        scorecard.right_score()
screen.exitonclick()