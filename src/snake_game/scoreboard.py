from turtle import Turtle
from config import SCREEN_HEIGHT, SIZE

ALIGN = 'center'
FONT= ('Courier', 14, "bold")
POSITION = SCREEN_HEIGHT/2 - SIZE

class Scoreboard(Turtle):
    def __init__(self) :      
      super().__init__()
      self.hideturtle()
      self.goto(0, POSITION)
      self.score=0
      self.color('white')
      self.write_scoreboard()
    
    def write_scoreboard(self):
      self.clear()
      self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)
       
    def increase_score(self):
       self.score += 1
       self.write_scoreboard()

    def game_over(self):
      
      self.goto(0, 0)
      self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

