from tkinter import *
import time
from math import *

mGui = Tk()
mGui.title('Elasticity Simulation')
mGui.geometry('1000x1000+100+100')

floor = 1000
canvas = Canvas(mGui, height=floor, width=1000, bg='white')
canvas.create_rectangle(0, 1000, 1000, floor, outline="#000000", fill="#75381a")
canvas.grid(row=0, column=0, rowspan=1000)

class Table:
    def draw(self):
        # code for creating table 
        for i in range(len(self.lst)): 
            for j in range(len(self.lst[i])): 
                  
                self.e = Entry(self.root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j + 1)
                self.e.insert(END, self.lst[i][j])

    def __init__(self, root):
        self.lst = [['Time', -1], 
           ['Height', -1], 
           ['# of Bounces', -1], 
           ['Velocity', -1], 
           ['Momentum', -1], 
           ['Kinetic Energy', -1], 
           ['Potential Energy', -1], 
           ['Mechanical Energy', -1]]
        self.root = root
        self.draw()

    def update(self, *args):
        for i in range(len(self.lst)):
            self.lst[i][1] = args[0][i]
        self.draw()

# create root window
table = Table(mGui)

preID = None
elasticity = 0.9
numBounces = 0
dropHeight = 1000
height = dropHeight
mass = 10
g = 9.8
v_after = sqrt(2 * g * height)
radius = 50
totalTime = 0
lastDrop = -1
iterations = 0
while True:
    if numBounces == 0:
        height = dropHeight - 1/2 * g * totalTime**2
    else:
        elapsed = totalTime - lastDrop
        height = radius + v_after * elapsed - 1/2 * g * elapsed**2

    if preID != None: canvas.delete(preID)
    height = max(height, radius)
    preID = canvas.create_oval(100, (floor - height) - radius, 100 + radius * 2, (floor - height) + radius)
    velocity = sqrt(max(v_after ** 2 - 2 * g * (height - radius), 0))
    KE = 1/2 * mass * velocity**2
    PE = mass * g * (height - radius)
    if iterations % 2 == 0: table.update([totalTime, height - radius, numBounces, velocity, mass * velocity, KE, PE, KE + PE])
    canvas.update()

    if height == radius:
        numBounces += 1
        lastDrop = totalTime
        v_after *= sqrt(elasticity)
    totalTime += 0.5
    time.sleep(0.05)
    iterations += 1
    if v_after < 1: break

print('done')

mGui.mainloop()