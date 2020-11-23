from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1024x576+10+30')

canvas_1 = Canvas(mGui,height=500,width=500,bg='grey')

canvas_1.pack()

pre = None
for i in range(1, 500):
    time.sleep(0.5)
    if pre != None:
        canvas_1.delete(pre)
    pre = canvas_1.create_oval(i,i,i+100,i+100)
    canvas_1.update()

mGui.mainloop()