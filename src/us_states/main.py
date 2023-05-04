import turtle
import pandas


screen = turtle.Screen()
screen.title("US states")
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

screen.setup(width=720, height=500)
# screen.bgcolor('gray')
# screen.tracer(0)

# turtle.onscreenclick(print)
# turtle.mainloop()

data = pandas.read_csv('50_states.csv')
print(data)
all_states =  data.state.to_list()
guessed_states = []

answer = screen.textinput(title="Name a state", prompt="Write a state's name" ).title()


while len(guessed_states)<50:
  print(answer)
  if answer == 'Exit':
    missing = [state    for state in all_states       if state not in guessed_states]
    new_data = pandas.DataFrame(missing, columns=['state'])
    new_data.to_csv('missing_states.csv')
    break
  if answer in all_states and answer not in guessed_states:
    guessed_states.append(answer)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state = data[data.state == answer]
    t.goto(int(state.x), int(state.y))
    t.write(answer)
    answer = screen.textinput(title =f"{len(guessed_states)}/50 states named", prompt="Good job! Write another state's name!",).title()
  else:    
    answer = screen.textinput(title =f"{len(guessed_states)}/50 states named", prompt="I am sorry, that's not quite right. Try again!").title()
