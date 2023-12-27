from turtle import Turtle
from game_ball import Ball
MOVE = 80
X_POS = 475
ball = Ball


class AI_Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.Y_POS = 0
        self.goto(X_POS, self.Y_POS)
        self.turtlesize(5, 0.5, None)

    def move(self, value):
        self.Y_POS = value
        if self.Y_POS >= 360 or self.Y_POS <= -360:
            pass
        else:
            self.goto(X_POS, self.Y_POS)
