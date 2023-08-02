from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

# window screen
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# right and left Paddle position
r_paddle = Paddle(position=(360, 0))
l_paddle = Paddle(position=(-360, 0))

# ball object from class
ball = Ball()

# right paddle controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# score object from class
score = Score()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)

    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() > -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

# PONG_GAME @Adhil03