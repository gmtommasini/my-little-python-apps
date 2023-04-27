from turtle import Turtle
from config import SCREEN_HEIGHT
STARTING_POSITION = (0, -180)
MOVE_DISTANCE = 40
FINISH_LINE_Y = 280


class Frog(Turtle):
    def __init__(self) -> None:
        super().__init__(shape='turtle')
        self.setheading(90)
        self.color('green')
        self.penup()
        self.goto_start()
                  
    def goto_start(self):
        self.goto(STARTING_POSITION)
    
    def up(self):
        self.goto(self.xcor(), self.ycor()  + MOVE_DISTANCE)
     
    def down(self):
        self.goto(self.xcor(), self.ycor()  - MOVE_DISTANCE)
        
    def left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor() )

    def right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
        
    def is_at_finish(self):
        if self.ycor() > SCREEN_HEIGHT:
            return True
        else: 
            return False
