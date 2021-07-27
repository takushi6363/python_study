import tkinter
import random

img = [None]*14
card = [0]*14

def set_card():
  r1 = random.randint(1,13)
  r2 = random.randint(1,13)
  cvs.create_image(400,180, image =img[card[r1]])
  cvs.create_image(400,420, image =img[card[r2]])

def shuffle_card():
   for i in range(13):
    card[i] = i

    
root =tkinter.Tk()
root.title("アップダウン")
root.resizable(False,False)
cvs = tkinter.Canvas(width=800,height=600,bg="green")
cvs.pack()
for i in range(14):
  img[i] = tkinter.PhotoImage(file=str(i)+".png")
shuffle_card()
set_card()
root.mainloop()