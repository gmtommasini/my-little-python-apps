import time
from turtle import Screen
from config import *
from frog import Frog
from car_manager import CarManager
from score import Scoreboard, Level

screen = Screen()
screen.title("FROG")
screen.setup(width=2*SCREEN_WIDTH, height=2*SCREEN_HEIGHT)
screen.bgcolor('gray')
screen.tracer(0)

level = Level()
frog = Frog()
car_manager = CarManager(level)
scoreboard=Scoreboard(level)

# Movement
screen.listen()
screen.onkey(frog.up, "Up")
screen.onkey(frog.down,"Down")
screen.onkey(frog.left,"Left")
screen.onkey(frog.right,"Right")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # Collision with car 
    for car in car_manager.all_cars:
        if car.distance(frog) < 30:
            game_is_on = False
            pass

    # Success cross
    if frog.is_at_finish():
        frog.goto_start()
        car_manager.level_up()
        scoreboard.level_up()
    