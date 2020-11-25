from tkinter import *
import time
from math import *

gui = Tk()
gui.title('Elasticity Simulation')
gui.geometry('1750x1000+10+10')

floor = 1000
canvas = Canvas(gui, height=floor, width=1000, bg='white')
canvas.grid(row=0, column=0, rowspan=1000)

class Parameters:
    def draw(self):
        # Initial Parameters
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=0 + 300, column=0 + 1)
        self.e.insert(END, self.lst[0][0])
        self.e.config(state=DISABLED)

        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=0 + 300, column=1 + 1)
        self.e.insert(END, self.lst[0][1])
        self.e.config(state=DISABLED)

        # Mass
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=1 + 300, column=0 + 1)
        self.e.insert(END, self.lst[1][0])
        self.e.config(state=DISABLED)

        self.mass = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.mass.grid(row=1 + 300, column=1 + 1)
        self.mass.insert(END, self.lst[1][1])

        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=1 + 300, column=2 + 1)
        self.e.insert(END, self.lst[1][2])
        self.e.config(state=DISABLED)

        # Elasticity
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=2 + 300, column=0 + 1)
        self.e.insert(END, self.lst[2][0])
        self.e.config(state=DISABLED)

        self.elas = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.elas.grid(row=2 + 300, column=1 + 1)
        self.elas.insert(END, self.lst[2][1])

        # Initial Height
        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=3 + 300, column=0 + 1)
        self.e.insert(END, self.lst[3][0])
        self.e.config(state=DISABLED)

        self.height = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.height.grid(row=3 + 300, column=1 + 1)
        self.height.insert(END, self.lst[3][1])

        self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold')) 
        self.e.grid(row=3 + 300, column=2 + 1)
        self.e.insert(END, self.lst[3][2])
        self.e.config(state=DISABLED)

    def __init__(self, root):
        self.lst = [['Initial Parameters', 'Enter Values:'], 
           ['Mass', 10, 'kg'],
           ['Elasticity', 0.5], 
           ['Initial Height', 900, 'm']]
        self.root = root
        self.draw()

    def read(self):
        return float(self.mass.get()), float(self.elas.get()), float(self.height.get());

    def enableTxt(self):
        self.mass.config(state=NORMAL)
        self.elas.config(state=NORMAL)
        self.height.config(state=NORMAL)

    def disableTxt(self):
        self.mass.config(state=DISABLED)
        self.elas.config(state=DISABLED)
        self.height.config(state=DISABLED)
param = Parameters(gui)

preID = None

started = False
paused = False
var = IntVar()
def startReset():
    global started
    global paused
    if not started:
        started = True
        paused = False
        startResetButton.config(text="Reset", bg="red")
        pausePlayButton.config(text="Pause")
        param.disableTxt()
        run(*param.read())
    else:
        global preID
        canvas.delete(preID)
        started = False
        paused = False
        startResetButton.config(text="Start", bg="green")
        pausePlayButton.config(text="Pause")
        param.enableTxt()
def pausePlay():
    global paused
    global var
    if not paused:
        paused = True
        pausePlayButton.config(text="Play")
        var = IntVar()
        pausePlayButton.wait_variable(var)
    else:
        paused = False
        pausePlayButton.config(text="Pause")
        var.set(1)

startResetButton = Button(text="Start", width=25, height=5, bg="green", fg="white", command = startReset)
pausePlayButton = Button(text="Pause", width=25, height=5, bg="grey", fg="white", command = pausePlay)

startResetButton.grid(row=925, column=1) #Start/reset
pausePlayButton.grid(row=925, column=2) #Pause/Play

class Table:
    def draw(self):
        for i in range(len(self.lst)): 
            for j in range(len(self.lst[i])):   
                self.e = Entry(self.root, width=20, fg='blue', font=('Arial',16,'bold'))   
                self.e.grid(row=i, column=j + 1)
                self.e.insert(END, self.lst[i][j])
                self.e.config(state=DISABLED)

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

    global preID
    numBounces = 0
    height = dropHeight
    g = 9.8
    v_after = sqrt(2 * g * height)
    radius = 50
    totalTime = 0
    lastDrop = -1
    iterations = 0

    while started:
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

gui.mainloop()