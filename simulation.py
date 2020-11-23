from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1000x1000+100+100')

canvas = Canvas(mGui,height=1000,width=1000,bg='white')
canvas.create_rectangle(0, 800, 1000, 1000, outline="#000000", fill="#75381a", width=2)
canvas.pack()

<<<<<<< HEAD
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
=======
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
>>>>>>> 1190a187f30e8b18323185094564ceccec273fe1

    elapsed += 0.1
    time.sleep(0.1)

mGui.mainloop()