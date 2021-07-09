import tkinter
from tkinter import font

FNT = ("Time New Roman", 40)
def move(e):
    cvs.delete("all")
    s = "({},{})".format(e.x, e.y)
    cvs.create_text(300,200,text=s,font=FNT)


root = tkinter.Tk()
root.title("マウスポインタの座標")
root.bind("<Motion>",move)
cvs = tkinter.Canvas(width=600,height=400)
cvs.create_text(300,200,text="ウィンド内でポインタを動かしてください")
cvs.pack()
cvs.mainloop()