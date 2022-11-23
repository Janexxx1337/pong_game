from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
screen.tracer(0)
game = True
score = 0

r_paddle = Paddle(365)
l_paddle = Paddle(-365)
ball = Ball()
scoreboard = Scoreboard()

screen.title('Ping-Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)


screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')


while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() - 320:
        ball.bounce_x()



    # Detect right_paddle missing
    if ball.xcor() > 380:
        ball.bounce_refresh()
        scoreboard.l_point()

    # Detect left_paddle missing
    elif ball.xcor() < - 380:
        ball.bounce_refresh()
        scoreboard.r_point()


screen.exitonclick()
