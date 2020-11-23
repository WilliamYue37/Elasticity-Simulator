from tkinter import *
import time
from math import *

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1000x1000+100+100')

floor = 1000
canvas = Canvas(mGui, height=floor, width=1000, bg='white')
canvas.create_rectangle(0, 1000, 1000, floor, outline="#000000", fill="#75381a", width=2)
canvas.grid(row=0, column=0, rowspan=1000)

class Table: 
      
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j + 1)
                self.e.insert(END, lst[i][j]) 
  
# take the data 
lst = [('Time', 19), 
       ('Height', 19), 
       ('# of Bounces', 19), 
       ('Velocity', 19), 
       ('Momentum', 19), 
       ('Kinetic Energy', 19), 
       ('Potential Energy', 19), 
       ('Mechanical Energy', 19)]
   
# find total number of rows and 
# columns in list 
total_rows = len(lst) 
total_columns = len(lst[0]) 
   
# create root window 
t = Table(mGui) 

preID = None
elasticity = 0.9
numBounces = 0
dropHeight = 1000
height = dropHeight
g = 9.8
v_after = sqrt(2 * g * height)
radius = 50
totalTime = 0
lastDrop = -1
while totalTime < 1000:
    if numBounces == 0:
        height = dropHeight - 0.5 * g * totalTime**2
    else:
        elapsed = totalTime - lastDrop
        height = radius + v_after * elapsed - 0.5 * g * elapsed**2

    if preID != None: canvas.delete(preID)
    height = max(height, radius)
    preID = canvas.create_oval(100, (floor - height) - radius, 100 + radius * 2, (floor - height) + radius)
    canvas.update()

    if height == radius:
        numBounces += 1
        lastDrop = totalTime
        v_after *= sqrt(elasticity)
    totalTime += 0.5
    time.sleep(0.05)


mGui.mainloop()