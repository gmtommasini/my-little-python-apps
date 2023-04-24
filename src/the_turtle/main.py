import turtle 
import random
from utils import random_color, extract_colors

directions = [0, 90, 180, 270]
t = turtle.Turtle()
t.speed(0)
t.pensize(10)
turtle.colormode(255)

# HIRST
colors = extract_colors()
def draw_hirst_dots(size=10, dot_size=10, distance_between_dots=10):
    dist = distance_between_dots + dot_size
    initial=-dist/2*size

    def dot():
      t.down()
      # t.color(random.choice(colors))
      t.dot(dot_size,random.choice(colors))
      t.up()

    def draw_line():
      for _ in range(size):
        dot()
        t.forward(dist)
       
    t.up()
    t.setheading(0)
    for i in range(size):
      print(f"i: {i}")
      t.setposition(initial,initial+ dist*i)
      draw_line()


draw_hirst_dots(5, 20, 20)


# HEART
def draw_heart(size):
    print(f"Draw heart {size}")
    if size<=0:
       return
    # Calculate the size of the heart
    factor = size / 20

    # Move turtle to starting position
    t.penup()
    t.goto(0, -150 * factor)
    t.pendown()

    # Draw the left side of the heart
    t.begin_fill()
    t.left(140)
    t.forward(177 * factor)
    t.circle(-90 * factor, 200)

    # Draw the right side of the heart
    t.left(120)
    t.circle(-90 * factor, 200)
    t.forward(177 * factor)
def draw_hearts():
  t.color('red')
  t.hideturtle()
  for r in range(0, 25):
    draw_heart(25 - r )
    t.color(random_color())
    t.setheading(0)
# draw_hearts()

# Spirograph
def draw_spirograph(gap, radius=100):
  for a in range(int(360/gap)):
    t.color(random_color())
    t.circle(radius)
    t.setheading(t.heading() + gap)
    print(t.heading())
# draw_spirograph(2)

# Random step
# for _ in range(300):
#   t.color(random_color())
#   # t.setheading(random.choice(directions))
#   t.setheading(random.randint(0,359))
#   t.forward(random.randint(10,50))

# N polygons
# for sides in range(3, 50):
#   a = 360 / sides
#   # t.write(str(sides) + " sides")
#   print(sides)
#   for x in range(sides):
#     color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
#     t.color(color)
#     t.forward(50)
#     t.right(a)

# dashed line
# for x in range(15):
#     t.forward(10)
#     t.up()
#     t.forward(10)
#     t.down()

# Square
# for x in range(4):
#   t.forward(100)
#   t.right(90)



s = turtle.Screen()  
s.exitonclick()