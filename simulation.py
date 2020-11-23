from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1000x1000+100+100')

canvas = Canvas(mGui,height=1000,width=1000,bg='white')
canvas.create_rectangle(0, 800, 1000, 1000, outline="#000000", fill="#75381a", width=2)
canvas.pack()

pre = None
x = 500
y = 50
v = 0
while y < 750:
    time.sleep(0.01)
    if pre != None:
        canvas.delete(pre)
    pre = canvas.create_oval(x-50,y-50,x+50,y+50, fill='#000000')
    canvas.update()
    y=y+v
    v=v+.098

mGui.mainloop()