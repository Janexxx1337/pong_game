from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


turtle = Turtle()
screen = Screen()
screen.tracer(0)
game = True

r_paddle = Paddle(365)
l_paddle = Paddle(-365)
ball = Ball()

screen.title('Ping-Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)




screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()



screen.exitonclick()
