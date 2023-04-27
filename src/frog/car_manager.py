from turtle import Turtle
from config import *
from score import Level
import random

class CarManager:
    def __init__(self, lvl:Level) -> None:
        self.all_cars = []
        self.car_speed =  STARTING_MOVE_DISTANCE
        self.level = lvl.get_level()
        
    def create_car(self):
        if random.randint(0,10) <= int(self.level):
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_LENGTH))
            new_car.color(random.choice(COLORS))
            random_Y = random.randint(-3, 3)*40
            new_car.goto(300, random_Y)
            self.all_cars.append(new_car)
            print(f"S: {self.car_speed}, L: {self.level}")
            print(f"Ncars: {len(self.all_cars)}")
            self.destroy_cars()
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.level +=1
        
    def destroy_cars(self):
        while self.all_cars and self.all_cars[0].xcor() < -(SCREEN_WIDTH+100):
            print("POP")
            self.all_cars.pop(0)
            
                