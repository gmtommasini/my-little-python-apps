from tkinter import *
from quiz_brain import QuizBrain
import os, sys
def file_path(rel_path):
  return os.path.join(sys.path[0], rel_path)

THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain : QuizBrain) -> None:
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title("Quizz")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_label.grid(row=0, column=1)
    
    self.canvas = Canvas(width=300, height=250, bg="white")
    self.question_text = self.canvas.create_text(
      150, 125, 
      width= 280,
      # text="Some text", 
      fill=THEME_COLOR,
      font=("Arial", 20, "italic")
      )
    self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    true_image =PhotoImage(file=file_path("images/true.png"))
    self.true_bt =Button(image=true_image, highlightthickness=0, command=self.true_pressed)
    self.true_bt.grid(row=2,column=0)

    false_image =PhotoImage(file=file_path("images/false.png"))
    self.false_bt =Button(image=false_image, highlightthickness=0, command=self.false_pressed)
    self.false_bt.grid(row=2,column=1)
    
    self.get_next_question()
    self.window.mainloop()
    
  def get_next_question(self) -> None:
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      self.enable_buttons()
      q_text=self.quiz.next_question()
      self.canvas.itemconfig(self.question_text,  text=q_text)
      self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.answereds}")
    else:
      self.canvas.itemconfig(self.question_text, text=f"THE END!\nYour final score is {self.quiz.score}/{self.quiz.answereds}")
      self.disable_buttons()
  
  def true_pressed(self):
    self.feedback(self.quiz.check_answer("True"))    
    
  def false_pressed(self):
    self.feedback(self.quiz.check_answer("False"))
    
  def feedback(self, is_correct: bool):
    self.disable_buttons()
    if is_correct:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_next_question)
      
  def disable_buttons(self):
      self.true_bt.config(state="disabled")
      self.false_bt.config(state="disabled")
  
  def enable_buttons(self):
      self.true_bt.config(state="normal")
      self.false_bt.config(state="normal")
  
    
    
if __name__ == "__main__":
  test = QuizInterface()