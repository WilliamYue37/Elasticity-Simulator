from tkinter import *
import time
from math import *

# setup the GUI and specify the window size
gui = Tk()
gui.title('Elasticity Simulation')
gui.geometry('1750x1000+10+10')

# set the elevation of the floor and initiate the Canvas
floor = 1000
canvas = Canvas(gui, height=floor, width=1000, bg='white')
canvas.grid(row=0, column=0, rowspan=1000) # set up the grid layout - the rowspan of 1000 is a hack to eliminate spacing between table rows

# parameter class for handing operations regarding the parameter table
class Parameters:
    def draw(self):
        # Initial Parameters
        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=0 + 300, column=0 + 1)
        self.e.insert(END, self.lst[0][0])
        self.e.config(state=DISABLED)

        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=0 + 300, column=1 + 1)
        self.e.insert(END, self.lst[0][1])
        self.e.config(state=DISABLED)

        # Mass
        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=1 + 300, column=0 + 1)
        self.e.insert(END, self.lst[1][0])
        self.e.config(state=DISABLED)

        self.mass = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.mass.grid(row=1 + 300, column=1 + 1)
        self.mass.insert(END, self.lst[1][1])

        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=1 + 300, column=2 + 1)
        self.e.insert(END, self.lst[1][2])
        self.e.config(state=DISABLED)

        # Elasticity
        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=2 + 300, column=0 + 1)
        self.e.insert(END, self.lst[2][0])
        self.e.config(state=DISABLED)

        self.elas = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.elas.grid(row=2 + 300, column=1 + 1)
        self.elas.insert(END, self.lst[2][1])

        # Initial Height
        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=3 + 300, column=0 + 1)
        self.e.insert(END, self.lst[3][0])
        self.e.config(state=DISABLED)

        self.height = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.height.grid(row=3 + 300, column=1 + 1)
        self.height.insert(END, self.lst[3][1])

        self.e = Entry(self.root, width=20, fg='blue', bg='LightBlue1', font=('Candara',16,'bold')) 
        self.e.grid(row=3 + 300, column=2 + 1)
        self.e.insert(END, self.lst[3][2])
        self.e.config(state=DISABLED)

    def __init__(self, root):
        self.lst = [['Initial Parameters', 'Enter Values:'], 
           ['Mass', 10, 'kg'],
           ['Elasticity ([0, 1])', 0.5], 
           ['Drop Height ([0, 900])', 900, 'm']]
        self.root = root
        self.draw()

    # used to read user input - return current parameters in the table cells
    def read(self):
        return float(self.mass.get()), float(self.elas.get()), float(self.height.get());

    # lets user edit the table cells
    def enableTxt(self):
        self.mass.config(state=NORMAL)
        self.elas.config(state=NORMAL)
        self.height.config(state=NORMAL)

    # prevents user from editing the table cells
    def disableTxt(self):
        self.mass.config(state=DISABLED)
        self.elas.config(state=DISABLED)
        self.height.config(state=DISABLED)
param = Parameters(gui) # initiate the parameter table

preID = None

# variables to store the state of the buttons
started = False
paused = False
var = IntVar()
def startReset(): # method to handle the clicking of the "start/reset" button
    global started
    global paused
    global table
    if not started:
        started = True
        paused = False
        startResetButton.config(text="Reset", bg="red")
        pausePlayButton.config(text="Pause",bg="grey")
        param.disableTxt()
        run(*param.read())
    else:
        global preID
        canvas.delete(preID)
        started = False
        paused = False
        table = Table(gui)
        startResetButton.config(text="Start", bg="blue")
        pausePlayButton.config(text="Pause", bg="grey")
        param.enableTxt()
def pausePlay(): # method to handle the clicking of the "start/reset" button
    global paused
    global var
    if not paused:
        paused = True
        pausePlayButton.config(text="Play", bg="green")
        var = IntVar()
        pausePlayButton.wait_variable(var)
    else:
        paused = False
        pausePlayButton.config(text="Pause", bg="grey")
        var.set(1)

# initialize the 2 buttons onto the GUI canvas
startResetButton = Button(text="Start", width=25, height=5, bg="blue", fg="white", font=('Candara', 11, 'bold'), command = startReset)
pausePlayButton = Button(text="Pause", width=25, height=5, bg="grey", fg="white", font=('Candara', 11, 'bold'), command = pausePlay)

startResetButton.grid(row=925, column=1) #Start/reset
pausePlayButton.grid(row=925, column=2) #Pause/Play

# class for the table containg values like momentum, kinetic energy, etc.
class Table:
	# method to update the table cells based on the values in the matrix "lst"
    def draw(self):
        for i in range(len(self.lst)): 
            for j in range(len(self.lst[i])):   
                self.mat[i][j].config(state=NORMAL)
                self.mat[i][j].delete(0, END)
                self.mat[i][j].insert(END, self.lst[i][j])
                self.mat[i][j].config(state=DISABLED)

    def __init__(self, root):
        self.lst = [['Time', 0, 's'], 
           ['Height', 0, 'm'], 
           ['# of Bounces', 0,], 
           ['Velocity', 0, 'm / s'], 
           ['Momentum', 0, 'kg * m / s'], 
           ['Kinetic Energy', 0, 'J'], 
           ['Potential Energy', 0, 'J'], 
           ['Mechanical Energy', 0, 'J']]
        self.root = root
        self.mat = [[0 for x in range(3)] for y in range(8)]
        for i in range(len(self.lst)): 
            for j in range(len(self.lst[i])):   
                self.mat[i][j] = Entry(self.root, width=20, fg='blue', font=('Candara',16,'bold'))   
                self.mat[i][j].grid(row=i, column=j + 1)
                self.mat[i][j].insert(END, self.lst[i][j])
                self.mat[i][j].config(state=DISABLED)
        self.draw()

    # update the class matrix "lst" with new values
    def update(self, *args):
        for i in range(len(self.lst)):
            self.lst[i][1] = args[0][i]
        self.draw()

table = Table(gui) # intialize the table

# method for controlling the movement of the ball
def run(mass, elasticity, dropHeight): # takes in initial parameters from user input through the parameter table
    # initialize variables
    global table
    global preID
    numBounces = 0
    g = 9.8
    v_after = sqrt(2 * g * dropHeight)
    radius = 50
    totalTime = 0
    lastDrop = -1
    iterations = 0

    # main loop to handle the movement of the ball at every instance of time
    while started:
    	# compute the height
        if numBounces == 0: # special case to handle inital drop
            height = dropHeight - 1/2 * g * totalTime**2
        else:
            elapsed = totalTime - lastDrop
            height = v_after * elapsed - 1/2 * g * elapsed**2

        if preID != None: canvas.delete(preID) # safety check
        height = max(height, 0) # ensures our ball doesn't go into the ground
        preID = canvas.create_oval(100, (floor - height) - radius * 2, 100 + radius * 2, floor - height, fill="purple", outline="purple")
        velocity = sqrt(max(v_after ** 2 - 2 * g * height, 0)) # compute the velocity
        if velocity < 1e-3 and height == 0: velocity = 0 # manually set the velocity to zero when the velocity becomes to small to see movement on the screen
        # compute values to update the table
        KE = 1/2 * mass * velocity**2
        PE = mass * g * height
        if iterations % 2 == 0 or velocity == 0 and height == 0: table.update([totalTime, height, numBounces, velocity, mass * velocity, KE, PE, KE + PE])
        if velocity == 0 and height < 1e-3: break # exit the loop when the movement of the ball is too neglible to been seen on the screen.
        canvas.update()

        # handle the change of velocity after the collision
        if height == 0:
            numBounces += 1
            lastDrop = totalTime
            v_after *= sqrt(elasticity)

        # update time and iteration variables
        totalTime += 0.5
        time.sleep(0.05) # slows the refresh rate so that machines with less powerful graphics won't see a deformation/glitch in the ball
        iterations += 1

gui.mainloop()