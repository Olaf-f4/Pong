import time
from turtle import Turtle, Screen
from player_paddle import Paddle
from game_ball import Ball
from AI import AI_Paddle

screen = Screen()
screen.setup(1050, 850)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
enemy = AI_Paddle()

screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    ball.move()
    enemy.move(ball.ycor())

    def cd_yaxis():
        heading = ball.heading()
        new_heading = 180 - heading
        ball.setheading(new_heading)
        ball.forward(100)

    def cd_xaxis():
        heading = ball.heading()
        new_heading = 360 - heading
        ball.setheading(new_heading)


    if ball.distance(paddle) < 40:
        cd_yaxis()
    if ball.distance(enemy) < 20:
        cd_yaxis()

    if ball.ycor() >= 375:
        cd_xaxis()
    elif ball.ycor() <= -375:
        cd_xaxis()

    if ball.xcor() >= 550 or ball.xcor() <= -550:
        print("Game Over")
        game_on = False

screen.exitonclick()
