from turtle import Turtle, Screen

t1 = Turtle()
screen =  Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place your bet", prompt="Whom do you think it will win the race?",  )



screen.exitonclick()