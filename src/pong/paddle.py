from turtle import Turtle
from config import P1_POSITION, P2_POSITION, SCREEN_HEIGHT, PADDLE_SPEED

class Paddle(Turtle):
    def __init__(self, player):
      super().__init__(shape='square')
      self.color('white')
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.up()
      self.set_paddles(player)
    
    def set_paddles(self, player):
      self.y_move = 0
      if player == 1:
        self.setposition(P1_POSITION,0)
      else:
        self.setposition(P2_POSITION,0)
       
    def move(self):
      ''' If not in the top and moving up, on not in the botton and moving down, then move'''
      if not ( (self.ycor() > SCREEN_HEIGHT/2-50 and self.y_move > 0) or\
              (self.ycor() < -SCREEN_HEIGHT/2+50 and self.y_move < 0) ):
          self.goto(self.xcor(), self.ycor() + self.y_move)
      else:
        self.y_move=0
    
    def go_up(self):
      if not self.y_move > 0:
        self.y_move += PADDLE_SPEED
      print(self.y_move)

    def go_down(self):
      if not  self.y_move < 0:
        self.y_move -= PADDLE_SPEED
      print(self.y_move)