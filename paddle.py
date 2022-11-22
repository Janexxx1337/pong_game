from turtle import Turtle

y_pos = 0


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.x_position = x_position
        self.color('white')
        self.shape('square')
        self.turtlesize(1.5, 7)
        self.settiltangle(90)
        self.penup()
        self.goto(x=self.x_position, y=0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

