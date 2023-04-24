from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SIZE

# Setting up 
screen = Screen()
screen.title("Snake")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Movement
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

speed = 0.2 # speed (higher = slower) = level
game_is_on = True

def game_over():
    global game_is_on 
    game_is_on = False
    scoreboard.game_over()
    print (" END GAME ")

while game_is_on:
    time.sleep(speed)
    snake.move()
    screen.update()
    
    # Colision with food
    if snake.head.distance(food) < SIZE - 1:
        snake.grow()
        food.new_food()
        scoreboard.increase_score()
   
#    Colision with wall
    if snake.head.xcor() >= SCREEN_WIDTH/2-SIZE\
        or snake.head.xcor() <= -SCREEN_WIDTH/2-SIZE\
        or snake.head.ycor() >= SCREEN_HEIGHT/2-SIZE\
        or snake.head.ycor() <= -SCREEN_HEIGHT/2-SIZE:
        game_over()
    
    # Colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_over()

    

     

        

    

screen.exitonclick()