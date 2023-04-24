from turtle import Turtle
from utils import random_position


FOOD_SIZE = 0.7
FOOD_COLOR = 'yellow'
FOOD_SHAPE = 'circle'

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE,stretch_wid=FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        self.goto(random_position())
        