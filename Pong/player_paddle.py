from turtle import Turtle
MOVE = 100
X_POS = -475

# when we are initializing a turtle object what are we doing?


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.Y_POS = 0
        self.goto(X_POS, self.Y_POS)
        self.turtlesize(5, 0.5, None)

        self.top = float(self.xcor() + 10)
        self.bottom = float(self.xcor() - 10)

    def up(self):
        self.Y_POS += MOVE
        if self.Y_POS >= 360:
            self.Y_POS -= MOVE
            pass
        else:
            self.goto(X_POS, self.Y_POS)

    def down(self):
        self.Y_POS -= MOVE
        if self.Y_POS <= -360:
            self.Y_POS += MOVE
            pass
        else:
            self.goto(X_POS, self.Y_POS)