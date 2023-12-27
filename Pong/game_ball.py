from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.start()

    def move(self):
        self.forward(20)

    def start(self):
        heading = random.randint(-180, 180)
        self.setheading(heading)
