from turtle import Turtle
from config import SCREEN_HEIGHT, SIZE, HIGH_SCORE_FILE

ALIGN = 'center'
FONT= ('Courier', 14, "bold")
POSITION = SCREEN_HEIGHT/2 - SIZE

class Scoreboard(Turtle):
    def __init__(self) :      
      super().__init__()
      self.hideturtle()
      self.goto(0, POSITION)
      self.score=0
      self.high_score=self.retrieve_high_score()
      self.color('white')
      self.write_scoreboard()
    
    def write_scoreboard(self):
      self.clear()
      self.write(f"Score = {self.score} High score: {self.high_score}", False, align=ALIGN, font=FONT)
       
    def increase_score(self):
       self.score += 1
       self.write_scoreboard()
    
    def reset(self):
      # updating high score
      if self.score > self.high_score:
        self.high_score = self.score
        self.set_high_score(self.high_score)
      self.score =0
      self.write_scoreboard()

    def game_over(self):      
      self.goto(0, 0)
      self.write(f"GAME OVER", False, align=ALIGN, font=FONT)

    def retrieve_high_score(self, file = HIGH_SCORE_FILE) -> int:
      try:
        with open(file, 'r') as f:
          score = f.read()
        return int(score)
      except FileNotFoundError:
        return 0
        
    def set_high_score(self, score, file = HIGH_SCORE_FILE) -> None:
      with open(file, 'w') as f:
        f.write(score)
      