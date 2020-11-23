from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1024x576+10+30')

canvas_1 = Canvas(mGui,height=500,width=500,bg='grey')

canvas_1.pack()

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

    if preID != None: canvas_1.delete(preID)
    preID = canvas_1.create_oval(100, height - radius, 100 + radius * 2, height + radius)
    canvas_1.update()

    elapsed += 0.1
    time.sleep(0.1)

mGui.mainloop()