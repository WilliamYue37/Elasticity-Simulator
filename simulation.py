from tkinter import *
import time

mGui = Tk()
mGui.title('GUI Example')
mGui.geometry('1000x1000+100+100')

canvas = Canvas(mGui,height=1000,width=1000,bg='white')
canvas.create_rectangle(0, 800, 1000, 1000, outline="#000000", fill="#75381a", width=2)
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