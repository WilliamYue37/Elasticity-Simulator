from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1000x1000+100+100')

canvas = Canvas(mGui,height=1000,width=1000,bg='white')
canvas.create_rectangle(0, 800, 1000, 1000, outline="#000000", fill="#75381a", width=2)
canvas.pack()

canvas.pack()

preID = None
numBounces = 0
dropHeight = 0
height = dropHeight
velocity = 0
radius = 50
g = 9.8
elapsed = 0
while elapsed < 50:
    if numBounces == 0:
        height = dropHeight + g * elapsed**2 / 2
    # else:

    if preID != None: canvas.delete(preID)
    preID = canvas.create_oval(100, height - radius, 100 + radius * 2, height + radius)
    canvas.update()

    elapsed += 0.1
    time.sleep(0.1)

mGui.mainloop()