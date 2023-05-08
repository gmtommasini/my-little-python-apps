from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 1000

current_card ={}
#  DATA
data = pandas.read_csv("data/french_words.csv")
to_learn =  data.to_dict(orient="records")


# Functions

def set_front_card():
  global current_card
  canvas.itemconfig(card_title, text="French", fill="black") 
  canvas.itemconfig(card_word, text=current_card["French"], fill="black")
  canvas.itemconfig(card_background, image=card_front_img )
  
def set_back_card():
  global current_card
  canvas.itemconfig(card_title, text="English", fill="white") 
  canvas.itemconfig(card_word, text=current_card["English"], fill="white")
  canvas.itemconfig(card_background, image=card_back_img )
  

def next_card():
  global current_card
  current_card=random.choice(to_learn)
  print(current_card["French"])
  set_front_card()
  timer()
  
def flip_card(event):
  title_config = canvas.itemconfig(card_title)["text"][4] 
  print(title_config)
  cancel_timer()
  if title_config == "French":
    set_back_card()
  else:
    set_front_card()
  

def timer():
    global flip_timer
    cancel_timer()
    flip_timer = window.after(3000, flip_card, "")
    
def cancel_timer():
    global flip_timer
    window.after_cancel(flip_timer)
  
#  UI
window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.bind("<Button-1>",  func=flip_card)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
check_image=PhotoImage(file="images/right.png")
unk_bt = Button(image=cross_image,highlightthickness=0, command=next_card)
check_bt=Button(image=check_image,highlightthickness=0, command=next_card)
unk_bt.grid(row=1, column=0)
check_bt.grid(row=1, column=1)

flip_timer=window.after(3000, flip_card, "")

next_card()
window.mainloop()
