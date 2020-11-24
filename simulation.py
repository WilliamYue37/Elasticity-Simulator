from tkinter import *
import time
from math import *

gui = Tk()
gui.title('Elasticity Simulation')
gui.geometry('1600x1000+10+10')

floor = 1000
canvas = Canvas(gui, height=floor, width=1000, bg='white')
canvas.grid(row=0, column=0, rowspan=1000)

paused = False
def buttonStart():
    global paused
    if paused:
        startStopButton.config(text="Start", bg="green")
        paused = False
    else:
        startStopButton.config(text="Stop", bg="red")
        paused = True
def buttonReset():
    print("reset")

startStopButton = Button(text="Start", width=25, height=5, bg="green", fg="white", command = buttonStart)
resetButton = Button(text="Reset", width=25, height=5, bg="grey", fg="white", command = buttonReset)

startStopButton.grid(row=925, column=1) #start/stop
resetButton.grid(row=925, column=2) #reset

class Parameters:
    def draw(self):
        # Initial Parameters
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=0 + 300, column=0 + 1)
        self.e.insert(END, self.lst[0][0])

        # Mass
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=1 + 300, column=0 + 1)
        self.e.insert(END, self.lst[1][0])

        self.mass = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.mass.grid(row=1 + 300, column=1 + 1)
        self.mass.insert(END, self.lst[1][1])

        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=1 + 300, column=2 + 1)
        self.e.insert(END, self.lst[1][2])

        # Elasticity
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=2 + 300, column=0 + 1)
        self.e.insert(END, self.lst[2][0])

        self.elas = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.elas.grid(row=2 + 300, column=1 + 1)
        self.elas.insert(END, self.lst[2][1])

        # Initial Height
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=3 + 300, column=0 + 1)
        self.e.insert(END, self.lst[3][0])

        self.height = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.height.grid(row=3 + 300, column=1 + 1)
        self.height.insert(END, self.lst[3][1])

        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=3 + 300, column=2 + 1)
        self.e.insert(END, self.lst[3][2])

    def __init__(self, root):
        self.lst = [['Initial Parameters'], 
           ['Mass', -1, 'kg'],
           ['Elasticity', -1], 
           ['Initial Height', -1, 'm']]
        self.root = root
        self.draw()

    def read(self):
        return float(self.mass.get()), float(self.elas.get()), float(self.height.get());

param = Parameters(gui)

class Table:
    def draw(self):
        for i in range(len(self.lst)): 
            for j in range(len(self.lst[i])):   
                self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold'))   
                self.e.grid(row=i, column=j + 1)
                self.e.insert(END, self.lst[i][j])

    def __init__(self, root):
        self.lst = [['Time', -1, 's'], 
           ['Height', -1, 'm'], 
           ['# of Bounces', -1,], 
           ['Velocity', -1, 'm / s'], 
           ['Momentum', -1, 'kg * m / s'], 
           ['Kinetic Energy', -1, 'J'], 
           ['Potential Energy', -1, 'J'], 
           ['Mechanical Energy', -1, 'J']]
        self.root = root
        self.draw()

    def update(self, *args):
        for i in range(len(self.lst)):
            self.lst[i][1] = args[0][i]
        self.draw()

def run(mass, elasticity, dropHeight):
    table = Table(gui)

    preID = None
    numBounces = 0
    height = dropHeight
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

run(mass = 10, elasticity = 0.8, dropHeight = 900)

gui.mainloop()