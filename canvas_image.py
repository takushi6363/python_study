import tkinter
root = tkinter.Tk()
root.title("キャンバスに画像を表示")
cvs = tkinter.Canvas(width=540,height=720)
test_image = tkinter.PhotoImage(file="test_image.png")
cvs.create_image(270,360,image=test_image)
cvs.pack()
root.mainloop()