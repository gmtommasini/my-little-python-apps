from tkinter import * 

FONT=("Arial", 24, 'bold')
w = Tk()
w.title("XIS")
w.minsize(400, 300)
w.config(padx=20, pady=20)

# Label
l=Label(text="THIS IS A LABEL", font=FONT)
l.grid(column=0,row=0)
l.config(pady=5)

# Button
def bt_click():
  new_text = input.get()
  l.config(text=new_text)

bt = Button(text="Click Me", command=bt_click)
bt.grid(column=10,row=1)
# Entry
input = Entry(width=10)
input.grid(column=3,row=3)

w.mainloop()