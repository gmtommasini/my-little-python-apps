from turtle import Screen, Turtle
import time
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SIZE, P1_POSITION, P2_POSITION
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Setting up 
screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0) # turns off animations

# Paddle
p1 = Paddle(1)
p2 = Paddle(2)
b = Ball()
sb =  Scoreboard()

screen.listen()
screen.onkey(p1.go_up, 'w')
screen.onkey(p1.go_down, 's')
screen.onkey(p2.go_up, 'Up')
screen.onkey(p2.go_down, 'Down')

game_on = True
while game_on:
    screen.update()
    b.move()
    p1.move()
    p2.move()
    time.sleep(b.move_speed)

    # colision with wall
    if b.ycor() > SCREEN_HEIGHT/2-SIZE or b.ycor() < -SCREEN_HEIGHT/2+SIZE:
        b.bounce_y()

    # colision with paddles
    if b.xcor() > P2_POSITION-30 and b.distance(p2) < 50 \
        or b.xcor() < P1_POSITION+30 and b.distance(p1) < 50:
        b.bounce_x()
    
    # detect p2 miss
    elif b.xcor() > SCREEN_WIDTH/2:
        b.reset_position()
        sb.p2_point()
    
    # detect p1 miss
    elif b.xcor() < -SCREEN_WIDTH/2:
        b.reset_position()
        sb.p1_point()

screen.exitonclick()