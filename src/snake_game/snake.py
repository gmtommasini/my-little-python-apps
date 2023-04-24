from turtle import Turtle
from config import *

START_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:

  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head=self.segments[0]

  def create_snake(self):
    for position in START_POSITION:
        self.add_segment(position)
     
  def add_segment(self, position):
    new_seg = Turtle('square')
    new_seg.color('white')
    new_seg.up()
    new_seg.goto(position)
    self.segments.append(new_seg)

  def grow(self):
    self.add_segment(self.segments[-1].position())
      

  def move(self):
    for seg in range(len(self.segments)-1, 0, -1):
        self.segments[seg].goto( self.segments[seg-1].position())       
    self.head.forward(SIZE)

  def up(self):
     if self.head.heading() != DOWN:
      self.head.setheading(UP)
     
  def down(self):
     if self.head.heading() != UP:
      self.head.setheading(DOWN)
     
  def left(self):
     if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
     if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
