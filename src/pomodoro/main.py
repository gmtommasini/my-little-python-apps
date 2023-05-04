from tkinter import *
from winsound import PlaySound, SND_ALIAS

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 30
CHECKMARK = '✔'
reps = 0
timer = None

# ------------------------------- UTILS ---------------------------------- # 

def beeb():
  # Beep(1500, 1000)
  PlaySound("SystemExclamation", SND_ALIAS)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  w.after_cancel(timer)  
  label.config( text=f"Timer", fg=PINK)
  checkmarks.config(text='')
  
  canvas.itemconfig(timer_text, text=f"{WORK_MIN:02d}:{0:02d}")
  reps = 0
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps +=1
  
  work_time = WORK_MIN * 60
  s_break = SHORT_BREAK_MIN * 60
  l_break =  LONG_BREAK_MIN * 60
  
  if reps %8 ==0: 
    # 4 cycles passed = 2h    
    label.config(text=f"Lunch Time!!", fg=GREEN)
    countdown(l_break)
    reps = 0
  elif reps%2 ==0:
    # second cycle means break
    label.config( text=f"Stretch.", fg=GREEN)
    countdown(s_break)
  else:
    label.config( text=f"Work!", fg=RED)
    countdown(work_time)
  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t):
  global timer
  t-=1
  canvas.itemconfig(timer_text, text=f"{int(t/60):02d}:{t%60:02d}")
  if t > 0:
    timer = w.after(10, countdown, t)
  else:
    checkmarks.config(text=CHECKMARK*int(reps/2))
    beeb()
    start_timer()
    
  


# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Pomodoro Timer")
w.config(padx=50, pady=25, bg=YELLOW)

label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
label.grid(column=2, row=1)

bg_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=250 , height=250, bg=YELLOW, highlightthickness=0)
canvas.create_image(125, 125, image=bg_image)
timer_text = canvas.create_text(125, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

checkmarks = Label( text='', font=(FONT_NAME, 15, 'bold'), bg=YELLOW, fg=GREEN)
checkmarks.grid(column=2, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)


w.mainloop()